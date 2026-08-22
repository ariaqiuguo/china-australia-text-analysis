import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from text_pipeline import analyse_row, classify_stage, clean_text


class TextPipelineTests(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("a\n  b"), "a b")

    def test_stage_boundaries(self):
        self.assertEqual(classify_stage("2016-12-01"), "1972-2016")
        self.assertEqual(classify_stage("2017-01-01"), "2017-2021")
        self.assertEqual(classify_stage("2024"), "2022-present")

    def test_frame_counts(self):
        result = analyse_row({"date": "2024", "title": "Australia dialogue", "text": "cooperation"})
        self.assertTrue(result["australia_relevant"])
        self.assertGreater(result["cooperation_count"], result["friction_count"])


if __name__ == "__main__":
    unittest.main()
