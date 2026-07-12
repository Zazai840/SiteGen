from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        text = "# Cool title"
        self.assertEqual(extract_title(text), "Cool title")
    
    def test_extract_no_heading(self):
        