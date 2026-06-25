from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None: 
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("no children")
        else:
            res = []
            for children in self.children:
                res.append(children.to_html())
            children_html = "".join(res)
            return f"<{self.tag}>{children_html}</{self.tag}>"


        