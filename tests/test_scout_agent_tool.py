import csv
import tempfile
import unittest
from pathlib import Path

from scripts.scout_agent_tool import (
    REQUIRED_COLUMNS,
    calculate_lead_score,
    score_band,
    validate_scout_csv,
)


class ScoutAgentToolTests(unittest.TestCase):
    def test_valid_empty_csv_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scout-leads.csv"
            path.write_text(",".join(REQUIRED_COLUMNS) + "\n")
            result = validate_scout_csv(path)
            self.assertEqual(result["status"], "success")

    def test_missing_column_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scout-leads.csv"
            path.write_text("lead_id,venue_name,status\n")
            result = validate_scout_csv(path)
            self.assertEqual(result["status"], "blocked")
            self.assertEqual(result["code"], "SCOUT_SOURCE_INCOMPLETE")

    def test_invalid_status_needs_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scout-leads.csv"
            with path.open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=REQUIRED_COLUMNS)
                writer.writeheader()
                row = {column: "" for column in REQUIRED_COLUMNS}
                row["lead_id"] = "VC-001"
                row["venue_name"] = "Example Room"
                row["city"] = "Ventura"
                row["county"] = "Ventura"
                row["region_priority"] = "1"
                row["status"] = "maybe"
                writer.writerow(row)
            result = validate_scout_csv(path)
            self.assertEqual(result["status"], "needs_review")
            self.assertTrue(any("maybe" in e for e in result["row_errors"]))

    def test_score_calculation(self):
        score = calculate_lead_score(
            books_live_bands=True,
            similar_bands_seen=True,
            target_region_fit=True,
            clear_booking_contact=True,
            music_style_fit=True,
            supports_six_piece=True,
        )
        self.assertEqual(score, 95)
        self.assertEqual(score_band(score), "high_priority")

    def test_score_deductions(self):
        score = calculate_lead_score(
            books_live_bands=True,
            wrong_music_programming=True,
            no_clear_contact=True,
        )
        self.assertEqual(score, 0)
        self.assertEqual(score_band(score), "weak")


if __name__ == "__main__":
    unittest.main()
