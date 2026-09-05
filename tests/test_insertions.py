"""Run with: python -m unittest discover -s tests"""
import copy
import importlib.util
from pathlib import Path
import unittest

script = Path(__file__).resolve().parents[1] / "plugins/dreaming-course-pipeline/scripts/validate_insertions.py"
spec = importlib.util.spec_from_file_location("insertions", script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InsertionChecks(unittest.TestCase):
    def test_valid_and_invalid_plans(self):
        row = dict(id=1, source="lecture.pptx", insert_before_slide=3,
                   sequence=1, frame=1, frame_count=2, story_text="word " * 40,
                   narration="word " * 40, concept_connection="state changes",
                   character_bible="Two distinct birds", visual_direction="Readable panels")
        second = dict(row, id=2, frame=2)
        plan = {"sources": [{"source": "lecture.pptx", "slide_count": 5}],
                "insertions": [row, second]}
        self.assertEqual(module.validate(plan)["final_slides"], 7)
        for key, value in [("insert_before_slide", 9), ("source", "missing.pptx"),
                           ("frame", 1), ("frame_count", 3), ("id", 4),
                           ("story_text", "A decorative slogan."),
                           ("character_bible", "Different characters")]:
            broken = copy.deepcopy(plan)
            broken["insertions"][1][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                module.validate(broken)


if __name__ == "__main__":
    unittest.main()
