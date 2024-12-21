block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def block_to_block_type(markdown):
    count = 0
    for character in markdown[:6]:
        if character == "#":
            count += 1
        else:
            break
    if 1 <= count <= 6 and markdown[count] == ' ':
        return block_type_heading
    if markdown[:3] == "```" and markdown [-3:] == "```":
        return block_type_code
    splited_markdown = markdown.split('\n')
    line_count_q = 0
    for line in splited_markdown:
        if line.startswith('>'):
            line_count_q += 1
    if line_count_q == len([line for line in splited_markdown if line]):
        return block_type_quote
    #unordered list block
    line_count_ul = 0
    for line in splited_markdown:
        if line.startswith('* ') or line.startswith('- '):
            line_count_ul += 1
    if line_count_ul == len([line for line in splited_markdown if line]):
        return block_type_ulist 
    expected_number = 1

    for line in splited_markdown:
        # Split the line at the first space to parse potential list items
        parts = line.split('. ', 1)
        if len(parts) == 2 and parts[0].isdigit() and int(parts[0]) == expected_number:
            expected_number += 1
        else:
            break

    # If expected_number matches the number of non-empty lines plus 1, it's an ordered list
    if expected_number == len([line for line in splited_markdown if line]) + 1:
        return block_type_olist
    else:
        return block_type_paragraph
        