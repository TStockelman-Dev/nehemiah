from enum import Enum
from markdown_to_blocks import markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from split_nodes_delimiter import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    stripped_block = block.strip()
    if stripped_block.startswith("#"):
        return BlockType.HEADING
    elif stripped_block.startswith("```"):
        return BlockType.CODE
    elif stripped_block.startswith(">"):
        return BlockType.QUOTE
    elif stripped_block.startswith("- ") or stripped_block.startswith("* "):
        return BlockType.UNORDERED_LIST
    elif stripped_block[0].isdigit() and stripped_block[1:3] == ". ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def inline_nodes(text):
    return [
        text_node_to_html_node(node)
        for node in text_to_textnodes(text)
    ]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))
            html_nodes.append(LeafNode(tag=f"h{level}", value=block.strip("# ").strip()))
        elif block_type == BlockType.PARAGRAPH:
            paragraph_text = " ".join(block.splitlines())
            html_nodes.append(ParentNode(tag="p", children=inline_nodes(paragraph_text)))
        elif block_type == BlockType.CODE:
            code_content = block[3:-3]
            if code_content.startswith("\n"):
                code_content = code_content[1:]
            html_nodes.append(ParentNode(tag="pre", children=[LeafNode(tag="code", value=code_content)]))
        elif block_type == BlockType.QUOTE:
            quote_content = block.strip("> ").strip()
            html_nodes.append(LeafNode(tag="blockquote", value=quote_content))
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for item in block.split("\n"):
                item = item.strip()
                if not item:
                    continue
                list_items.append(item[2:].strip())
            html_nodes.append(ParentNode(
                tag="ul",
                children=[
                    ParentNode(tag="li", children=inline_nodes(item))
                    for item in list_items
                ],
            ))
        elif block_type == BlockType.ORDERED_LIST:
            list_items = [
                item.strip().split(". ", 1)[1]
                for item in block.split("\n")
                if item.strip()
            ]
            html_nodes.append(ParentNode(
                tag="ol",
                children=[
                    ParentNode(tag="li", children=inline_nodes(item))
                    for item in list_items
                ],
            ))
    return ParentNode(tag="div", children=html_nodes)