import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_image(self):
        node = TextNode("", TextType.IMAGE, url="some url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "some url", "alt": ""} )
    
    def test_unsuitable_text_type(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a node with unsuitable text type", "invalid text type")
            text_node_to_html_node(node)
                
                            

if __name__ == "__main__":
    unittest.main()
