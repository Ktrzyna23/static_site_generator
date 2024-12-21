class HTMLNode:
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f'{key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        if value is None:
            raise ValueError("Value is required")
        super().__init__(tag, value,None ,props)
            
    def to_html(self):
        props_html = ""
        if self.tag is None:
            return f"{self.value}"
        if self.props is not None:
            for prop in self.props:
                props_html += f'{prop}="{self.props[prop]}"'
                if props_html == "":
                    return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
                else:    
                    return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self,tag, children = None, props = None):
        if tag is None:
            raise ValueError("Tag is required")
        if children is None:
            raise ValueError("Children value missing!")
        super().__init__(tag, None, children ,props)
    def to_html(self):
        text = ""
        props_html = ""
        for child in self.children:
            text += child.to_html()

        # Build the props HTML if props exist
        if self.props is not None:
            for prop in self.props:
                props_html += f' {prop}="{self.props[prop]}"'

        # Return the final HTML with all children
        return f"<{self.tag}{props_html}>{text}</{self.tag}>"





        
        
        
        
        
        
        
        if self.tag is None:
            return f"{self.value}"
        if self.props is not None:
            for prop in self.props:
                props_html += f'{prop}="{self.props[prop]}"'
                if props_html == "":
                    return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
                else:    
                    return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"      





    


    