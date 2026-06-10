import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_props_to_html(self):
        node = HTMLNode("str", "val", ["children"], {"val" : "prop"})
        self.assertEqual(node.props_to_html(), ' val="prop"')
        node2 = HTMLNode()
        self.assertEqual(node2.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("str", "val", ["children"], {"val" : "prop"})
        self.assertEqual(node.__repr__(), "HTMLNode(str, val, ['children'], {'val': 'prop'})")


if __name__ == "main":
    unittest.main()