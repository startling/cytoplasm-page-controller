# import the defaults from cytoplasm
from cytoplasm.defaults import *

# a markdown interpreter
import markdown
markdown_extensions = ['abbr', 'footnotes', 'toc', 'fenced_code', 'headerid']

@Interpreter("markdown", "md")
def markdown_interpreter(file, destination):
    markdown.markdownFromFile(input=file, output=destination,
            extensions = markdown_extensions, encoding="utf8", safe=False)

controllers = [
    ("page", ["_pages", "_build", "_templates"]),
]
