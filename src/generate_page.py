from markdown_to_html import *
from main import basepath
import os
                
def generate_page(from_path, template_path, dest_path, basepath):
    
    print(f"generating page from from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        page_content = f.read()
    with open(template_path) as t: 
        template = t.read()
    
    html_content = markdown_to_html_node(page_content)
    html_string = html_content.to_html()
    
    title = extract_title(page_content)
    content = template.replace("{{ Title }}", f"{title}")
    content = content.replace("{{ Content }}", f"{html_string}")
    content = content.replace('href="/', f"href={basepath}")
    content = content.replace('src="/', f"src={basepath}")
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, "w") as c:
        c.write(content)

def extract_title(text):
    lines = text.split("\n")
    if lines[0].startswith("#"):
        return lines[0][determine_heading_level(lines[0]) + 1:]
    else:
        raise Exception("no heading")
    
def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    for content in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, content)
        
        destination = os.path.join(dest_dir_path, content)
    
        if os.path.isfile(source_path):
            if os.path.splitext(source_path)[1] == ".md":
                dest_filename = os.path.splitext(destination)[0] + ".html"
                generate_page(source_path, template_path, dest_filename, basepath)
        else:
            generate_pages_recursively(source_path, template_path, destination, basepath)