from markdown_to_blocks import markdown_to_blocks
from block_to_block import *
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_type_dict = {}
    parent_node = HTMLNode(tag='div')  # Step 1: Create a parent node
    block_type_dict = {block: block_to_block_type(block)}
    for block in blocks:
        
        for block in block_type_dict:
            if block_to_block_type(block) == block_type_paragraph:
                node =  HTMLNode("p", block, None, None)
                parent_node.add_child(node)
            elif block_to_block_type(block) == block_type_heading:
                count = 0
                for character in block[:6]:
                    if character == "#":
                        count += 1
                tag = f'h{count}'
                text_without_hashes = block[count:].strip()
                heading_node = HTMLNode(tag=tag, value=text_without_hashes)
                parent_node.add_child(heading_node)
            elif block_to_block_type(block) == block_type_code:
                code_node = HTMLNode(tag='code', value=block)
                node_code = HTMLNode(tag='pre')
                node_code.add_child(code_node)
                parent_node.add_child(node_code)
            elif block_to_block_type(block) == block_type_quote:
                node_quote = HTMLNode(tag='blockquote', value=block)
                parent_node.add_child(node_quote)
            elif block_to_block_type(block) == block_type_ulist:
                ul_node = HTMLNode(tag='ul')
                # Assuming you have a way to split the block into individual items
                list_items = block.splitlines()  # Or use the appropriate splitting method
                for item in list_items:
                    li_node = HTMLNode(tag='li', value=item.strip("* ").strip())
                    ul_node.add_child(li_node)
                parent_node.add_child(ul_node)
            elif block_to_block_type(block) == block_type_olist:
                ol_node = HTMLNode(tag='ol')
                # Similarly split the block into individual items
                list_items = block.splitlines()  # Adjust split logic as needed
                for item in list_items:
                    li_node = HTMLNode(tag='li', value=item.strip("1234567890. ").strip())
                    ol_node.add_child(li_node)
                parent_node.add_child(ol_node)
    return parent_node
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode(tag='div')  # Step 1: Create a parent node

    for block in blocks:
        block_type = block_to_block_type(block)  # Assign block type once
        
        if block_type == block_type_paragraph:
            node = HTMLNode("p", block)
            parent_node.add_child(node)
        
        elif block_type == block_type_heading:
            count = 0
            for character in block[:6]:
                if character == "#":
                    count += 1
            tag = f'h{count}'
            text_without_hashes = block[count:].strip()
            heading_node = HTMLNode(tag=tag, value=text_without_hashes)
            parent_node.add_child(heading_node)
        
        elif block_type == block_type_code:
            code_node = HTMLNode(tag='code', value=block)  # Assuming no leading spaces
            node_code = HTMLNode(tag='pre')
            node_code.add_child(code_node)
            parent_node.add_child(node_code)
        
        elif block_type == block_type_quote:
            node_quote = HTMLNode(tag='blockquote', value=block.strip("> ").strip())  # Assume > for quote
            parent_node.add_child(node_quote)
        
        elif block_type == block_type_ulist:
            ul_node = HTMLNode(tag='ul')
            list_items = block.splitlines()
            for item in list_items:
                li_node = HTMLNode(tag='li', value=item.strip("* ").strip())
                ul_node.add_child(li_node)
            parent_node.add_child(ul_node)
        
        elif block_type == block_type_olist:
            ol_node = HTMLNode(tag='ol')
            list_items = block.splitlines()  # Adjust split logic as needed
            for item in list_items:
                li_node = HTMLNode(tag='li', value=item.strip("1234567890. ").strip())
                ol_node.add_child(li_node)
            parent_node.add_child(ol_node)
    return parent_node
