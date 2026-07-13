from markdown_to_html import determine_heading_level

def extract_title(text):
    lines = text.split("\n")
    if lines[0].startswith("#"):
        return lines[0][determine_heading_level(lines[0]) + 1:]
    else:
        raise Exception("no heading")
