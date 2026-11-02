from textwrap import dedent


def markdown_to_blocks(markdown):
    return [
        block.strip()
        for block in dedent(markdown).split("\n\n")
        if block.strip()
    ]