import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_repr(self):
        node = LeafNode("a", "Cool spot", {'key' : 'val'})
        self.assertEqual(node.__repr__(), "LeafNode(a,Cool spot, {'key': 'val'})")