from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        text = "# Cool title"
        self.assertEqual(extract_title(text), "Cool title")
    
    def test_extract_no_heading(self):
        text = "this is text with no heading"
        with self.assertRaises(Exception):
            extract_title(text)
    
    def test_extract_heading_levels(self):
        text = "### This is a h3 heading"
        self.assertEqual(extract_title(text), "This is a h3 heading")