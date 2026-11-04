from content_copy import content_copy
from content_generation_engine import generate_pages_recursive

def main():
    content_copy("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()