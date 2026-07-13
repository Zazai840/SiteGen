from textnode import TextNode
from copy_to_destination import copy_to_destination
from generate_page import generate_page
def main():
    copy_to_destination("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
