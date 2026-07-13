from markdown_to_blocks import *
from htmlnode import *
from textnode import *
from text_to_textnodes import *
from parentnode import *

def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(create_html_node_from_block(block, block_type))
    
    return ParentNode("div", html_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        child_node = text_node_to_html_node(node)
        children.append(child_node)

    return children

def determine_heading_level(block):
    count = 0
    c = 0 
    while count < len(block) and block[c] == "#":
        count += 1
        c += 1
    return count

def create_html_node_from_block(block, type):
    if type == BlockType.CODE:
        code = block.replace("```", "")
        stripped_code = code.lstrip("\n")
        code_node = LeafNode("code", stripped_code)
        return ParentNode("pre", [code_node])
    
    
    if type == BlockType.HEADING:
        level = determine_heading_level(block)
        heading_text = block[level + 1:]
        children = text_to_children(heading_text)
        if level in range(1, 7):
            return ParentNode(f"h{level}", children) 

    if type == BlockType.PARAGRAPH:
        paragraph_text = block.replace("\n", " ")
        children = text_to_children(paragraph_text)
        return ParentNode("p", children)

    if type == BlockType.QUOTE:
        quote_lines = block.split("\n")
        cleaned_lines = []
        for line in quote_lines:
            clean_line = line[2:]
            cleaned_lines.append(clean_line)
        cleaned_lines = " ".join(cleaned_lines)
        children = text_to_children(cleaned_lines)
        return ParentNode("blockquote", children)

    if type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        list_items = []
        for i in range(len(lines)):
            item_text = lines[i][2:]
            if lines[i].startswith(f"{i + 1}. "):
                item_children = text_to_children(item_text)
                list_items.append(ParentNode("li", item_children))
        return ParentNode("ol", list_items)


    if type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        list_items = []
        for line in lines:
            item_text = line[2:]
            item_children = text_to_children(item_text)
            list_items.append(ParentNode("li", item_children))
        return ParentNode("ul", list_items)











