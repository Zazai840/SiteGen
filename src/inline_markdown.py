from textnode import TextNode, TextType

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
        

