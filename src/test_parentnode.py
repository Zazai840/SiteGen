import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_nested_parents(self):
        nested_node = ParentNode("span", [LeafNode(None, "child")])
        node = ParentNode("div", [nested_node])
        self.assertEqual(node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_multiple_children(self):
        sibling_nodes = [LeafNode(None, f"child{i}") for i in range(5) ]
        node = ParentNode("div", sibling_nodes)
        self.assertEqual(node.to_html(), "<div>child0child1child2child3child4</div>")
    
    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    



    
