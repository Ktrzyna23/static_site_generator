import unittest
from combined_function import (
    text_to_textnodes,
    TextNode,
    TextType
)
from markdown_to_blocks import markdown_to_blocks
class TestTextToNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "This is plain text"
        expected = [
            TextNode("This is plain text", TextType.TEXT)
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual[0].text, expected[0].text)
        self.assertEqual(actual[0].text_type, expected[0].text_type)

    def test_text_with_bold(self):
        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if actual[i].text_type == TextType.LINK:
                self.assertEqual(actual[i].url, expected[i].url)
    def test_text_with_link(self):
        text = "This is a [link](https://boot.dev)"
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if actual[i].text_type == TextType.LINK:
                self.assertEqual(actual[i].url, expected[i].url)


    def test_text_to_textnodes(self):
            nodes = text_to_textnodes(
                "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
            )
            self.assertListEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                nodes,)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )




if __name__ == "__main__":
    unittest.main()