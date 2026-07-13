from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    
    print(f"generating page from from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        page_content = f.read()
    with open(template_path) as t: 
        template = t.read()
    html_content = markdown_to_html_node(page_content)
    html_string = html_content.to_html()
    
    title = extract_title(page_content)
    with_title = template.replace("{{ Title }}", f"{title}")
    with_content = with_title.replace("{{ Content }}", f"{html_string}")

    os.makedirs(os.path.dirname(dest_path), 511, True)
    
    with open(dest_path, "w") as c:
        c.write(with_content)
