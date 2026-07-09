import unittest
from markdown_to_blocks import *

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_irregular_spacing(self):
        md = """
This is a paragraph



This is a paragraph after three new lines




This is a paragraph after four new lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,["This is a paragraph", 
                                 "This is a paragraph after three new lines",
                                 "This is a paragraph after four new lines"])

    def test_markdown_to_blocks_white_space(self):
        md = """
              This is a paragraph with a lot of white space          


              This is another paragraph with a lot of white space              

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph with a lot of white space", 
                                  "This is another paragraph with a lot of white space"])




class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_to_block_type_code(self):
         block = "```\n This is a code block ```"
         self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_block_to_block_type_unordered_list(self):
        block = "- This here is an undordered list\n- This is the second item in the list\n- Let's see if this works"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This here is an ordered list\n2. Let's see if this works"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_block_to_block_type(self):
         block = "This is paragraph text"
         self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)