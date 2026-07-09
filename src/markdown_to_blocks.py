from enum import Enum

def markdown_to_blocks(text : str) -> list[str]:
    splitted_text = text.split('\n\n')
    stripped_splitted_text = []
    for text in splitted_text:
        stripped = text.strip()
        if stripped:
            stripped_splitted_text.append(stripped)
    return stripped_splitted_text
    

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block : str) -> BlockType:
    #check for heading
    count = 0
    c = 0
    while c < len(block) and block[c] == "#":
        count += 1 
        c += 1
    if c < len(block) and block[c] == " " and 1 <= count <= 6: 
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
        
    



