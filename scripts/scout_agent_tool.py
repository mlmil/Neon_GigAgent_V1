#!/usr/bin/env python3
"""Scout Agent lead CSV validator, scoring tool, and report generator.

Usage:
  python3 scripts/scout_agent_tool.py <csv_path>              # validate CSV
  python3 scripts/scout_agent_tool.py --score <csv_path>      # validate + emit stale/score warnings
  python3 scripts/scout_agent_tool.py --calc-score            # print scoring rubric help
  python3 scripts/scout_agent_tool.py --report <csv_path>     # generate weekly markdown report
  python3 scripts/scout_agent_tool.py --summary <csv_path>    # print summary stats
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Schema constants
# ---------------------------------------------------------------------------

REQUIRED_COLUMNS = [
    "lead_id",
    "venue_name",
    "city",
    "county",
    "region_priority",
    "status",
    "lead_score",
    "gig_type",
    "source_type",
    "source_url",
    "similar_bands_seen",
    "booking_contact_name",
    "booking_contact_email",
    "booking_contact_phone",
    "lead_owner",
    "next_action",
    "follow_up_date",
    "last_checked",
    "notes",
]

REQUIRED_NONEMPTY = ["lead_id", "venue_name", "city", "county", "region_priority", "status"]

ALLOWED_STATUSES = {
    "discovered",
    "researching",
    "qualified",
    "ready_to_contact",
    "contacted",
    "follow_up",
    "warm",
    "not_a_fit",
    "booked",
    "converted_to_venue_agent",
}

ALLOWED_GIG_TYPES = {"club", "festival", "municipal", "private_club"}

ALLOWED_SOURCE_TYPES = {
    "venue_website",
    "venue_calendar",
    "venue_social",
    "local_event_listing",
    "band_social",
    "chamber_of_commerce",
    "parks_rec",
    "fraternal_org",
    "referral",
    "other",
}

ALLOWED_OWNERS = {"Mike Miller", "Alfred Morlaes", "Curtis Clyde", "unassigned"}

ALLOWED_REGION_PRIORITIES = {"1", "2", "3"}

STALE_DAYS = 60
DATE_FORMAT = "%Y-%m-%d"


# ---------------------------------------------------------------------------
# Scoring rubric
# ---------------------------------------------------------------------------

SCORING_RUBRIC = {
    "adds": {
        "books_live_bands":          25,
        "similar_bands_seen":        20,
        "target_region_fit":         15,
        "clear_booking_contact":     15,
        "music_style_fit":           10,
        "supports_six_piece":        10,
        "high_value_gig_type":       15,
        "warm_connection_notes":      5,
    },
    "subtracts": {
        "no_clear_contact":         -20,
        "wrong_music_programming":  -20,
        "too_far":                  -15,
        "one_off_no_recurring":     -15,
        "do_not_contact":           -50,
    },
    "bands": {
        "high_priority":  (80, 100),
        "qualified":      (60, 79),
        "research_more":  (40, 59),
        "weak":           (0, 39),
    },
}


def calculate_lead_score(
    books_live_bands: bool = False,
    similar_bands_seen: bool = False,
    target_region_fit: bool = False,
    clear_booking_contact: bool = False,
    music_style_fit: bool = False,
    supports_six_piece: bool = False,
    high_value_gig_type: bool = False,
    warm_connection_notes: bool = False,
    no_clear_contact: bool = False,
    wrong_music_programming: bool = False,
    too_far: bool = False,
    one_off_no_recurring: bool = False,
    do_not_contact: bool = False,
) -> int:
    """Calculate a Scout lead score (0-100) from known signals."""
    r = SCORING_RUBRIC
    score = 0
    if books_live_bands:       score += r["adds"]["books_live_bands"]
    if similar_bands_seen:     score += r["adds"]["similar_bands_seen"]
    if target_region_fit:      score += r["adds"]["target_region_fit"]
    if clear_booking_contact:  score += r["adds"]["clear_booking_contact"]
    if music_style_fit:        score += r["adds"]["music_style_fit"]
    if supports_six_piece:     score += r["adds"]["supports_six_piece"]
    if high_value_gig_type:    score += r["adds"]["high_value_gig_type"]
    if warm_connection_notes:  score += r["adds"]["warm_connection_notes"]
    if no_clear_contact:       score += r["subtracts"]["no_clear_contact"]
    if wrong_music_programming: score += r["subtracts"]["wrong_music_programming"]
    if too_far:                score += r["subtracts"]["too_far"]
    if one_off_no_recurring:   score += r["subtracts"]["one_off_no_recurring"]
    if do_not_contact:         score += r["subtracts"]["do_not_contact"]
    return max(0, min(100, score))


def score_band(score: int) -> str:
    """Return human-readable priority band for a score."""
    if score >= 80:
        return "high_priority"
    if score >= 60:
        return "qualified"
    if score >= 40:
        return "research_more"
    return "weak"


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def _parse_date(val: str) -> date | None:
    try:
        return datetime.strptime(val.strip(), DATE_FORMAT).date()
    except (ValueError, AttributeError):
        return None


def read_leads(path: Path) -> tuple[list[dict], list[str]]:
    """Read rows and fieldnames from CSV."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    return rows, fieldnames


def validate_scout_csv(path: Path, check_scores: bool = False) -> dict:
    """Validate the Scout lead CSV."""
    warnings: list[str] = []
    row_errors: list[str] = []

    if not path.exists():
        return {
            "status": "blocked",
            "code": "FILE_NOT_FOUND",
            "failure_reason": f"File not found: {path}",
            "warnings": [],
            "row_errors": [],
        }

    rows, fieldnames = read_leads(path)

    # Column presence check
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
    if missing_cols:
        return {
            "status": "blocked",
            "code": "SCOUT_SOURCE_INCOMPLETE",
            "failure_reason": f"Missing columns: {', '.join(missing_cols)}",
            "warnings": [],
            "row_errors": [],
        }

    today = date.today()
    seen_lead_ids = set()

    for i, row in enumerate(rows, start=2):
        lead_id = row.get("lead_id", "").strip()
        ref = f"Row {i} ({lead_id or '?'} / {row.get('venue_name', '?')})"

        # Duplicate ID check
        if lead_id:
            if lead_id in seen_lead_ids:
                row_errors.append(f"{ref}: duplicate lead_id '{lead_id}'")
            seen_lead_ids.add(lead_id)

        # Required non-empty fields
        for field in REQUIRED_NONEMPTY:
            if not row.get(field, "").strip():
                row_errors.append(f"{ref}: '{field}' is empty")

        # Status
        status = row.get("status", "").strip()
        if status and status not in ALLOWED_STATUSES:
            row_errors.append(f"{ref}: invalid status '{status}'")

        # Gig type
        gig_type = row.get("gig_type", "").strip()
        if gig_type and gig_type not in ALLOWED_GIG_TYPES:
            row_errors.append(f"{ref}: invalid gig_type '{gig_type}'")

        # Source type
        source_type = row.get("source_type", "").strip()
        if source_type and source_type not in ALLOWED_SOURCE_TYPES:
            row_errors.append(f"{ref}: invalid source_type '{source_type}'")

        # Lead owner
        owner = row.get("lead_owner", "").strip()
        if owner and owner not in ALLOWED_OWNERS:
            row_errors.append(f"{ref}: invalid lead_owner '{owner}'")

        # Region priority
        priority = row.get("region_priority", "").strip()
        if priority and priority not in ALLOWED_REGION_PRIORITIES:
            row_errors.append(f"{ref}: invalid region_priority '{priority}' (must be 1, 2, or 3)")

        # Lead score range
        score_raw = row.get("lead_score", "").strip()
        if score_raw:
            try:
                score_val = int(score_raw)
                if not (0 <= score_val <= 100):
                    row_errors.append(f"{ref}: lead_score {score_val} out of range (0-100)")
            except ValueError:
                row_errors.append(f"{ref}: lead_score '{score_raw}' is not an integer")

        # Date fields
        for date_field in ("follow_up_date", "last_checked"):
            val = row.get(date_field, "").strip()
            if val and _parse_date(val) is None:
                row_errors.append(f"{ref}: {date_field} '{val}' not in YYYY-MM-DD format")

        # Stale lead warning
        last_checked_val = row.get("last_checked", "").strip()
        if last_checked_val:
            last_checked_date = _parse_date(last_checked_val)
            if last_checked_date and (today - last_checked_date).days > STALE_DAYS:
                days_old = (today - last_checked_date).days
                warnings.append(
                    f"{ref}: last_checked is {days_old} days ago (>{STALE_DAYS} day threshold)"
                )

    if row_errors:
        return {
            "status": "needs_review",
            "code": "SCOUT_ROW_ERRORS",
            "failure_reason": f"{len(row_errors)} row error(s) found",
            "warnings": warnings,
            "row_errors": row_errors,
        }

    return {
        "status": "success",
        "warnings": warnings,
        "row_errors": [],
    }


# ---------------------------------------------------------------------------
# Report generation & Summary
# ---------------------------------------------------------------------------

def generate_report_markdown(path: Path) -> str:
    """Generate Markdown Scout report from leads CSV."""
    rows, _ = read_leads(path)
    
    # Sort leads by score descending
    valid_rows = []
    for r in rows:
        try:
            score = int(r.get("lead_score", "0"))
        except ValueError:
            score = 0
        valid_rows.append((score, r))
    valid_rows.sort(key=lambda x: x[0], reverse=True)

    today_str = date.today().strftime("%Y-%m-%d")
    lines = [
        f"# Scout Agent Weekly Report - {today_str}",
        "",
        "## Executive Summary",
        f"- **Total Active Leads Tracked**: {len(rows)}",
        f"- **High Priority Leads (Score 80+)**: {sum(1 for s, _ in valid_rows if s >= 80)}",
        f"- **Qualified Leads (Score 60-79)**: {sum(1 for s, _ in valid_rows if 60 <= s < 80)}",
        "",
        "## Top New Leads",
        "| Lead ID | Venue Name | City / County | Score | Status | Next Action |",
        "|---|---|---|---|---|---|",
    ]

    for score, row in valid_rows[:10]:
        lines.append(
            f"| `{row.get('lead_id')}` | **{row.get('venue_name')}** | {row.get('city')}, {row.get('county')} | {score} | `{row.get('status')}` | {row.get('next_action')} |"
        )

    lines.extend([
        "",
        "## Best Leads To Contact First (Ready For Outreach Review)",
    ])
    ready_leads = [row for score, row in valid_rows if row.get("status") in ("ready_to_contact", "qualified") and score >= 70]
    if ready_leads:
        for row in ready_leads[:5]:
            lines.extend([
                f"### {row.get('venue_name')} ({row.get('city')}, {row.get('county')}) - Score: {row.get('lead_score')}",
                f"- **Gig Type**: {row.get('gig_type')}",
                f"- **Contact**: {row.get('booking_contact_name') or 'N/A'} ({row.get('booking_contact_email') or row.get('booking_contact_phone') or 'No direct email'})",
                f"- **Source URL**: [{row.get('source_type')}]({row.get('source_url')})",
                f"- **Similar Bands**: {row.get('similar_bands_seen') or 'None noted'}",
                f"- **Notes**: {row.get('notes')}",
                "",
            ])
    else:
        lines.append("_No leads currently marked ready_to_contact._\n")

    lines.extend([
        "## Similar Bands / Venue Signals",
        "- Bands spotted across target circuit: " + ", ".join(sorted(set(
            b.strip() for _, r in valid_rows for b in r.get("similar_bands_seen", "").split(",") if b.strip()
        ))) or "_None recorded yet._",
        "",
        "## Follow-Ups Due",
    ])
    followups = [row for _, row in valid_rows if row.get("follow_up_date")]
    if followups:
        for row in followups:
            lines.append(f"- **{row.get('venue_name')}**: Follow-up scheduled for {row.get('follow_up_date')} (`{row.get('status')}`)")
    else:
        lines.append("- _No specific follow-up dates pending._")

    lines.extend([
        "",
        "## Dead Ends / Not A Fit",
    ])
    not_fits = [row for _, row in valid_rows if row.get("status") == "not_a_fit"]
    if not_fits:
        for row in not_fits:
            lines.append(f"- **{row.get('venue_name')}**: {row.get('notes')}")
    else:
        lines.append("- _No disqualified venues recorded in this period._")

    lines.extend([
        "",
        "## Needs Mike Decision",
        "- Review `ready_to_contact` leads above for outreach approval.",
        "- Confirm booking owner assignment before any communication is drafted.",
        "",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Scout lead CSV, score leads, and generate reports."
    )
    parser.add_argument("csv_path", nargs="?", help="Path to scout-leads.csv")
    parser.add_argument(
        "--score",
        action="store_true",
        help="Include stale-lead warnings in output",
    )
    parser.add_argument(
        "--calc-score",
        action="store_true",
        help="Print scoring rubric and exit",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate weekly Markdown report",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print summary statistics of the leads file",
    )
    args = parser.parse_args()

    if args.calc_score:
        print(json.dumps(SCORING_RUBRIC, indent=2))
        return 0

    if not args.csv_path:
        parser.print_help()
        return 1

    path = Path(args.csv_path)
    result = validate_scout_csv(path, check_scores=args.score)

    if args.report:
        if result["status"] == "blocked":
            print(json.dumps(result, indent=2))
            return 1
        print(generate_report_markdown(path))
        return 0

    if args.summary:
        if result["status"] == "blocked":
            print(json.dumps(result, indent=2))
            return 1
        rows, _ = read_leads(path)
        print(f"Total leads: {len(rows)}")
        statuses: dict[str, int] = {}
        for r in rows:
            st = r.get("status", "unknown")
            statuses[st] = statuses.get(st, 0) + 1
        for st, count in sorted(statuses.items()):
            print(f"  {st}: {count}")
        return 0

    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
