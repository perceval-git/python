import re
from docx import Document
from sys import argv

def find_all_templates(document):
    templates = set()
    for paragraph in document.paragraphs:
        for match in re.finditer('\\{\\{.*?\\}\\}', paragraph.text):
            templates.add(match.group(0))

    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                templates += find_all_templates(cell)
                #for match in re.search('\\{\\{.*?\\}\\}', cell):
                #    templates.add(match.group(0))

    return templates

def docx_replace_regex(document, regex, replace):
    for p in document.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex , replace)



def main():
    filename = 'test.docx'
    if len(argv) >= 2:
        filename = argv[-1]
    doc = Document(filename)

    replacements = {}
    for template in find_all_templates(doc):
        replacement = input('Replace {} with: '.format(template))
        replacements[template] = replacement

    for template, replacement in replacements.items():
        docx_replace_regex(doc, re.compile(template), replacement)

    doc.save('test-output.docx')

if __name__ == '__main__':
    main()