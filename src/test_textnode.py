import unittest
from regex import *
from textnode import TextNode, TextType, text_node_to_html_node
from split_delimiter import *
from split_imgages_links import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2, "najs łan 1 test zakończony")
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "wow")
        node2 = TextNode("This is a text node", TextType.BOLD, "wow")
        self.assertEqual(node, node2, "najs łan 2 test zakończony")
    def test_not_eq(self):
        # Create two TextNode objects with different attributes
        node1 = TextNode("This is a text node", TextType.BOLD, "wow")
        node2 = TextNode("This is a different text node", TextType.BOLD, "wow")
        
        # Assert that they are not equal
        self.assertNotEqual(node1, node2, "najs łan 3 test zakończony")

        # Test with different text_type
        node3 = TextNode("This is a text node", TextType.ITALIC, "wow")
        self.assertNotEqual(node1, node3, "najs łan 4 test zakończony")

        # Test with different URL
        node4 = TextNode("This is a text node", TextType.BOLD, "different_url")
        self.assertNotEqual(node1, node4, "najs łan 5 test zakończony")



    def test_text_node_to_html_node2(self):
        # test normal text
        node = TextNode("text", TextType.LINK, "https://boot.dev")
        html = text_node_to_html_node(node)
        assert html.tag == "a"
        assert html.value == "text"
        assert html.props == {"href":"https://boot.dev"}


    def test_text_node_to_html_node3(self):
        # test normal text
        node = TextNode("text", TextType.IMAGE, "https://boot.dev/IMG.PNG")
        html = text_node_to_html_node(node)
        assert html.tag == "img"
        assert html.value == ""
        assert html.props == {"src":"https://boot.dev/IMG.PNG", "alt": "text"}



    def test_split_nodes_delimiter_basic(self):
            node = TextNode("This is a `code block` example", TextType.TEXT)
            result = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual(result, [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" example", TextType.TEXT)
            ])

    def test_split_nodes_delimiter_missing(self):
        node = TextNode("This `string has unmatched delimiters", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue("Invalid Markdown syntax: unmatched delimiter" in str(context.exception))

    def test_split_nodes_delimiter_no_delimiters(self):
        node = TextNode("This has no code blocks", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This has no code blocks", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode("Here `is` a `test` case", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Here ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" a ", TextType.TEXT),
            TextNode("test", TextType.CODE),
            TextNode(" case", TextType.TEXT)
        ])
class TestMarkdownExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Test cases for extract_markdown_images
        self.assertEqual(
            extract_markdown_images("This is text with a ![alt text](http://example.com/image.jpg)."),
            [("alt text", "http://example.com/image.jpg")]
        )
        self.assertEqual(
            extract_markdown_images("![image1](https://example.com/img1.png) and ![image2](https://example.com/img2.png)"),
            [("image1", "https://example.com/img1.png"), ("image2", "https://example.com/img2.png")]
        )
        self.assertEqual(
            extract_markdown_images("No images here."),
            []
        )
        self.assertEqual(
            extract_markdown_images("![empty alt]()"),
            [("empty alt", "")]
        )

    def test_extract_markdown_links(self):
        # Test cases for extract_markdown_links
        self.assertEqual(
            extract_markdown_links("This is a [link](http://example.com)."),
            [("link", "http://example.com")]
        )
        self.assertEqual(
            extract_markdown_links("[link1](https://example.com/1) and [link2](https://example.com/2)"),
            [("link1", "https://example.com/1"), ("link2", "https://example.com/2")]
        )
        self.assertEqual(
            extract_markdown_links("This is text without links."),
            []
        )
        self.assertEqual(
            extract_markdown_links("This is an image ![not a link](http://example.com/image.jpg)."),
            []
        )
        self.assertEqual(
            extract_markdown_links("[empty link]()"),
            [("empty link", "")]
        )
class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_link_single(self):
        node = TextNode("Check this out [Boot.dev](https://www.boot.dev)!", TextType.TEXT)
        result = split_nodes_link([node])

        expected = [
            TextNode("Check this out ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
            TextNode("!", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode("Links: [Link A](urlA) and [Link B](urlB).", TextType.TEXT)
        result = split_nodes_link([node])

        expected = [
            TextNode("Links: ", TextType.TEXT),
            TextNode("Link A", TextType.LINK, "urlA"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Link B", TextType.LINK, "urlB"),
            TextNode(".", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_split_nodes_link_none(self):
        node = TextNode("No links here!", TextType.TEXT)
        result = split_nodes_link([node])

        expected = [TextNode("No links here!", TextType.TEXT)]

        self.assertEqual(result, expected)


    # You would also implement similar tests for split_nodes_image
if __name__ == "__main__":
    unittest.main()