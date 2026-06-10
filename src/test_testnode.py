import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_input_equality(self):
        node = TextNode("Hello", TextType.BOLD, "url")
        node2 = TextNode("Bye", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)
    
    def test_url_equality(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is text", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)

    def test_type_equality(self):
        node = TextNode("Text", TextType.BOLD)
        node2 = TextNode("Text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is node", TextType.CODE, "youtube.com")
        self.assertEqual(
            "TextNode(This is node, code, youtube.com)", repr(node)
        )    
    


if __name__ == "__main__":
    unittest.main()
