# PROJECT_CONTEXT.md

## What This Project Is

`Neon_Gig_Agent_v1` is the prospecting and venue discovery agent for **Neon Blonde** (a 6-piece energetic retro, dance, and rock party band). It finds and qualifies potential live music venues, private clubs, festivals, and municipal concert series in target regions before they graduate to the booking pipeline.

## Current Goal

Operate `Neon_Gig_Agent_v1` to discover, qualify, score (0–100), and track high-probability venue opportunities across the California coastal reach spanning **San Francisco to San Diego**, focused on Priority 1 territories (Ventura County, Santa Barbara County, Malibu, and Calabasas).

## Important People Or Stakeholders

- **Mike Miller**: Band leader, primary approval gate for outreach and confirmed bookings.
- **Alfred Morlaes**: Band booking / outreach partner.
- **Curtis Clyde**: Occasional booking lead.

## Important Files And Folders

- `SCOUT_AGENT.md`: Operating handbook and rules for `Neon_Gig_Agent_v1`.
- `scout-leads.csv`: Primary database of tracked venue leads.
- `do-not-contact.csv`: Blacklisted or disqualified venues.
- `schemas/scout_leads_schema.json`: Schema definition with region prefixes (`MAL`, `CAL`, `VC`, `SB`, `SFV`, `LA`, `CC`).
- `scripts/scout_agent_tool.py`: CLI tool for CSV validation, lead scoring, and weekly report generation.
- `regions/`: Regional dossiers for Malibu/Calabasas, Ventura County, Santa Barbara County, LA Valley, and Central Coast.
- `reports/`: Weekly generated Scout reports.

## Repeated Tasks

- **Lead Research**: Finding new venues from public calendars, websites, and peer band schedules.
- **Lead Validation**: Running `python3 scripts/scout_agent_tool.py scout-leads.csv`.
- **Reporting**: Generating weekly Scout summaries (`python3 scripts/scout_agent_tool.py --report scout-leads.csv`).

## Known Gotchas

- **Scout Scope Guardrails**: Leads are strictly prospects. No outreach emails, calendar edits, or booking confirmations are permitted without Mike's approval.
- **Venue Sizing**: Neon Blonde is a 6-piece full electric band; ensure venue stages and sound setups accommodate the band footprint.

## Useful Commands

```bash
# Validate leads CSV
python3 scripts/scout_agent_tool.py scout-leads.csv

# Summary breakdown
python3 scripts/scout_agent_tool.py --summary scout-leads.csv

# Generate weekly report
python3 scripts/scout_agent_tool.py --report scout-leads.csv

# Run test suite
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Success Criteria

This project is successful when:
1. `scout-leads.csv` consistently tracks qualified, scored leads across target territories.
2. Weekly Scout reports clearly present the top candidates ready for outreach review.
3. All operations adhere to Mike's human approval gate.
