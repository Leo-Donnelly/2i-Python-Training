import unittest

class TestMoodDiary(unittest.TestCase):
    def setUp(self):
        self.name = "Leo"
        self.feeling = "happy"
        self.path = r"C:\Users\LeoDonnelly\OneDrive - 2i Limited\Documents\Python Iniative\2i-Python-Training\Updated Python Course\Beginner\Module 3\2025-11-13.txt"

        with open(self.path, 'r') as file:
            self.content = file.read()
    
    def test_diary_name(self):
        self.assertIn(self.name, self.content)

    def test_diary_contains_feeling(self):
        self.assertTrue(self.feeling in self.content)
    
    def test_diary_starts_dear_diary(self):
        self.assertTrue(self.content.startswith("Dear Diary"))

    def test_output_is_string(self):
        self.assertIsInstance(self.content, str)

if __name__ == "__main__":
    unittest.main()
    