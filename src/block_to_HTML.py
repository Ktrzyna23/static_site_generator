from markdown_to_blocks import markdown_to_blocks
from block_to_block import *
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_type_dict = {}
    for block in blocks:
        block_type_dict = {block: block_to_block_type(block)}
    for block in block_type_dict:
        if block_to_block_type(block) == block_type_paragraph:
            HTMLNode("p", block, None, None)
        if block_to_block_type(block) == block_type_heading:
            count = 0
            for character in block[:6]:
                if character == "#":
                    count += 1
            tag = f'h{count}'
            text_without_hashes = block[count:].strip()
            heading_node = HTMLNode(tag=tag, value=text_without_hashes)
        if block_to_block_type(block) == block_type_code:
            HTMLNode("pre")

