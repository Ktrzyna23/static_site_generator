from enum import Enum
from htmlnode import HTMLNode , LeafNode , ParentNode
class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6
class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            raise ValueError("text_type must be of TextType")
        self.url = url
    def __eq__(self, target):
        if self.text == target.text and self.text_type == target.text_type and self.url == target.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {(self.text_type).value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise Exception("Invalid text node")
    if text_node.text_type not in TextType:
        raise Exception("Invalid text node")
    

    if text_node.text_type == TextType.TEXT:
        return LeafNode("", text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "" , props)
