import json
import unittest
from pathlib import Path

from sys import path
path.insert(0, str(Path(__file__).parents[1] / "src"))

from catalog import search, validate


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_path = Path(__file__).parents[1] / "data" / "collateral.json"
        cls.records = json.loads(data_path.read_text())

    def test_search_returns_current_stage_and_use_case_match(self):
        result = search(
            self.records,
            stage="consideration",
            use_case="answer_manual_reporting_objection",
        )
        self.assertEqual([record["version"] for record in result], ["2.1"])

    def test_archived_version_is_not_returned(self):
        result = search(self.records, stage="consideration")
        self.assertTrue(all(record["status"] == "current" for record in result))

    def test_sample_catalog_is_valid(self):
        self.assertEqual(validate(self.records), [])

    def test_missing_metadata_is_reported(self):
        broken = [dict(self.records[0], owner="")]
        self.assertIn("owner", validate(broken)[0])


if __name__ == "__main__":
    unittest.main()
