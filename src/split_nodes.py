from extract_markdown import *
from textnode import *

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