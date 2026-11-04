from content_copy import content_copy
from content_generation_engine import generate_pages_recursive
import sys

default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    content_copy("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()