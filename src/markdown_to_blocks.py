def markdown_to_blocks(markdown):
    result = []
    current_lines = []
    for line in markdown.splitlines():
        if line.strip() != "":
            current_lines.append(line.strip())
        else:
            # only append if we have content
            if current_lines:
                result.append("\n".join(current_lines))
                current_lines = []
    
    # don't forget the last block!
    if current_lines:
        result.append("\n".join(current_lines))
    
    return result
 