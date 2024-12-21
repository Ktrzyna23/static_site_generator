from textnode import TextNode, TextType
from htmlnode import HTMLNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for text_node in old_nodes:
        if text_node.text_type != TextType.TEXT:
            result.append(text_node)
            continue
            
        text = text_node.text
        start = text.find(delimiter)
        if start == -1:
            result.append(text_node)  # Keep the original node if no delimiter found
            continue
            
        end = text.find(delimiter, start + len(delimiter))
        if end == -1:
            raise Exception("Invalid Markdown syntax: unmatched delimiter")
            
        # Only add text before delimiter if non-empty
        before_text = text[:start]
        if before_text:
            result.append(TextNode(before_text, TextType.TEXT))
            
        # Only add text between delimiters if non-empty
        between_text = text[start + len(delimiter):end]
        if between_text:
            result.append(TextNode(between_text, text_type))
        
        # Only process remaining text if non-empty
        remaining_text = text[end + len(delimiter):]
        if remaining_text:
            result.extend(split_nodes_delimiter([TextNode(remaining_text, TextType.TEXT)], delimiter, text_type))
    return result
        
        
        #if len(output) % 2 == 0:  # Even number of segments implies missing delimiter
        #    raise Exception("Invalid Markdown syntax: unmatched delimiter")
        #for index, segment in enumerate(output):
            # Alternate between types based on the index parity
        #    if index % 2 == 1:  # Odd index for text inside delimiters
        #        result.append(TextNode(segment, text_type))
         #   else:  # Even index for text outside delimiters
        #        if segment:  # Only append if there's content
         #           result.append(TextNode(segment, TextType.TEXT))

            
