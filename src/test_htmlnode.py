import unittest

from htmlnode import HTMLNode , LeafNode , ParentNode







class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("UA", 12, [], {})
        node2 = HTMLNode("UA", 12, [], {})
        self.assertEqual(node, node2, "najs łan 1 test zakończony")
    def test_eq2(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2, "najs łan 2 test zakończony")
    def test_not_eq(self):
        # Create two TextNode objects with different attributes
        node1 = HTMLNode("UA", 12,[], {})
        node2 = HTMLNode("UA", 13, None , None )
        
        # Assert that they are not equal
        self.assertNotEqual(node1, node2, "najs łan 3 test zakończony")

        # Test with different text_type
        node3 = HTMLNode("UA",25 , [] , {})
        self.assertNotEqual(node1, node3, "najs łan 4 test zakończony")

        # Test with different URL
        node4 = HTMLNode(None, None, None, None)
        self.assertNotEqual(node1, node4, "najs łan 5 test zakończony")

class TestLeafNode(unittest.TestCase):
    def test_valid_leaf_node(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_valid_parent_node(self):
        node = ParentNode("p",     [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_valid_parent_node2(self):
        node = ParentNode("p",     [
        LeafNode("D", "Italic text"),
        ],{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><D>Italic text</D></p>')

    def test_missing_tag_raises_error(self):
        # Using assertRaises to check if ValueError is raised
        with self.assertRaisesRegex(ValueError,"Tag is required"):
            node = ParentNode(None, [LeafNode("b", "some text")])
            node.to_html() 
    def test_missing_tag_raises_error(self):
        # Using assertRaises to check if ValueError is raised
        with self.assertRaisesRegex(ValueError,"Children value missing!"):
            node = ParentNode("B", None)
            node.to_html() 

if __name__ == "__main__":
    unittest.main()