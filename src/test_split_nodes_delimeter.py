import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class test_split_nodes_delimiter(unittest.TestCase):
    def test_code_text(self):
        test_node = TextNode("this is a `code block` that is being tested", TextType.TEXT)
        res = split_nodes_delimiter([test_node], "`", TextType.CODE)
        expected_res = [TextNode("this is a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" that is being tested", TextType.TEXT)]
        self.assertEqual(res, expected_res)
    
    def test_bold_text(self):
        test_node = TextNode("this is **bold text** that is being tested", TextType.TEXT)
        res = split_nodes_delimiter([test_node], "**", TextType.BOLD)
        expected_res = [TextNode("this is ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" that is being tested", TextType.TEXT)]
        self.assertEqual(res, expected_res)
    
    def test_italic_text(self):
        test_node = TextNode("this is _italic text_ that is being tested", TextType.TEXT)
        res = split_nodes_delimiter([test_node], "_", TextType.ITALIC)
        expected_res = [TextNode("this is ", TextType.TEXT), TextNode("italic text", TextType.ITALIC), TextNode(" that is being tested", TextType.TEXT)]
        self.assertEqual(res, expected_res)

    def test_delimiter_at_beginning_of_text(self):
        test_node = test_node = TextNode("_italic text_ that is being tested", TextType.TEXT)
        res = split_nodes_delimiter([test_node], "_", TextType.ITALIC)
        expected_res = [TextNode("italic text", TextType.ITALIC),
                        TextNode(" that is being tested", TextType.TEXT)]
        self.assertEqual(res, expected_res)

   
