from textnode import *
from split_nodes import *


def text_to_textnodes(text):
   text_as_node = TextNode(text, TextType.TEXT)
   nodes = split_nodes_delimiter([text_as_node], "**", TextType.BOLD)
   nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
   nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
   nodes = split_nodes_image(nodes)
   nodes = split_nodes_link(nodes)
   return nodes
