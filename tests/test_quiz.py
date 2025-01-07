import unittest
from qcm.question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        question = Question("Test question?", ["Option 1", "Option 2", "Option 3"], "a")
        self.assertTrue(question.is_correct("a"))
        self.assertFalse(question.is_correct("b"))

    def test_shuffle_options(self):
        question = Question("Test question?", ["Option 1", "Option 2", "Option 3"], "a")
        original_options = question.options[:]
        question.shuffle_options()
        self.assertNotEqual(original_options, question.options)
        self.assertIn("Option 1", question.options)
        self.assertIn("Option 2", question.options)
        self.assertIn("Option 3", question.options)

if __name__ == "__main__":
    unittest.main()