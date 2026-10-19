from enum import Enum

class TextType(Enum):
    Plain = "text/plain",
    Bold = "**Bold text**",
    Italic = "_Italic text_",
    Code_Text = "`Code text`",
    Links = "[anchor text](url)",
    Images = "![alt text](url)",

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"