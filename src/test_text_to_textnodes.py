import unittest
from text_to_textnodes import *
from textnode import *

class TestTexttoTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        sample_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(sample_text), [TextNode("This is ", TextType.TEXT),
                                                                   TextNode("text", TextType.BOLD),
                                                                   TextNode(" with an ", TextType.TEXT),
                                                                   TextNode("italic", TextType.ITALIC),
                                                                   TextNode(" word and a ", TextType.TEXT),
                                                                   TextNode("code block", TextType.CODE),
                                                                   TextNode(" and an ", TextType.TEXT),
                                                                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                                                    TextNode(" and a ", TextType.TEXT),
                                                                    TextNode("link", TextType.LINK, "https://boot.dev"),
])
        
    def test_text_to_textnodes_plain_text(self):
        sample_text = "This is plain text that is being tested"
        self.assertListEqual(text_to_textnodes(sample_text), [TextNode("This is plain text that is being tested", TextType.TEXT)])

    def test_text_to_textnodes_no_image(self):
        sample_text = "This is text with **bold** text, _italic_ text, text that is `code` and also [links](https://youtube.com), but no images"
        self.assertListEqual(text_to_textnodes(sample_text), [TextNode("This is text with ", TextType.TEXT), 
                                                              TextNode("bold", TextType.BOLD), 
                                                              TextNode(" text, ",TextType.TEXT), 
                                                              TextNode("italic", TextType.ITALIC),
                                                              TextNode(" text, text that is ", TextType.TEXT),
                                                              TextNode("code", TextType.CODE),
                                                              TextNode(" and also ", TextType.TEXT),
                                                              TextNode("links", TextType.LINK, "https://youtube.com"),
                                                              TextNode(", but no images", TextType.TEXT)])
