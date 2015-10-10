__author__ = 'siwei'

import docx

class DocConcerter:
    def __init__(self):
        "123"

    def convertFromDocx(self, file_name):
        document = docx.Document(file_name)
        docText = '\n'.join([
            paragraph.text.encode('utf-8') for paragraph in document.paragraphs if paragraph.text != ""
        ])
        print docText

if __name__ == "__main__":
    x = DocConcerter()
    x.convertFromDocx("cv/SIWEI.docx")