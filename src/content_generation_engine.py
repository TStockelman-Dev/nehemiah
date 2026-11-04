import os
from markdown_blocks import markdown_to_html_node
from split_nodes_delimiter import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as content_file:
        md_content = content_file.read()

    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()


    html_nodes = markdown_to_html_node(md_content)
    nodes = html_nodes.to_html()

    extracted_title = extract_title(md_content)
    template_content = template_content.replace("{{ Title }}", extracted_title)
    template_content = template_content.replace("{{ Content }}", nodes)

    destination_dir = os.path.dirname(dest_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as new_file:
        new_file.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path[:-3] + ".html")
                generate_page(from_path, template_path, dest_path)