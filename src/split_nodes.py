from extract_markdown import *
from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        split_string = node.text.split(delimiter)
        if len(split_string) % 2 == 0:
            raise ValueError("invalid markdown") 
        
        for i in range(len(split_string)):
            if i % 2 == 0:
                if split_string[i] != "":
                    node = TextNode(split_string[i], TextType.TEXT)
                    new_list.append(node)
            else:
                if split_string[i] != "":
                    node = TextNode(split_string[i], text_type)
                    new_list.append(node)

    return new_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res_text_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            res_text_nodes.append(node)
            continue
        original_text = node.text
        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                res_text_nodes.append(TextNode(sections[0], TextType.TEXT))
            res_text_nodes.append(TextNode(f"{image_alt}", TextType.IMAGE, f"{image_link}"))
            original_text = sections[1]
        if original_text:
            res_text_nodes.append(TextNode(original_text, TextType.TEXT))
    return res_text_nodes
            
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res_text_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            res_text_nodes.append(node)
            continue
        original_text = node.text
        for link_alt, link_link in links:
            sections = original_text.split(f"[{link_alt}]({link_link})", 1)
            if sections[0] != "":
                res_text_nodes.append(TextNode(sections[0], TextType.TEXT))
            res_text_nodes.append(TextNode(f"{link_alt}", TextType.LINK, f"{link_link}"))
            original_text = sections[1]
        if original_text:
            res_text_nodes.append(TextNode(original_text, TextType.TEXT))
    return res_text_nodes