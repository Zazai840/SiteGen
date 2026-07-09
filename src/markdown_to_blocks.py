def markdown_to_blocks(text):
    splitted_text = text.split('\n\n')
    stripped_splitted_text = []
    for text in splitted_text:
        stripped = text.strip()
        if stripped:
            stripped_splitted_text.append(stripped)
    return stripped_splitted_text
    


    
    

