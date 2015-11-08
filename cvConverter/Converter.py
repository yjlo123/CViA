from cvConverter.DOCFileConverter import DOCFileConverter
from cvConverter.DOCXFileConverter import DOCXFileConverter
from cvConverter.PDFFileConverter import PDFFileConverter
from cvConverter.TXTFileConveryer import TXTFileConverter

__author__ = 'siwei'

class DocConverter:
    def __init__(self):
        self.converters = []
        self.add_converters()

    def add_converters(self):
        doc_converter = DOCFileConverter()
        self.converters.append(doc_converter)
        docx_converter = DOCXFileConverter()
        self.converters.append(docx_converter)
        txt_converter = TXTFileConverter()
        self.converters.append(txt_converter)
        pdf_converter = PDFFileConverter()
        self.converters.append(pdf_converter)

    def get_extension(self, file_name):
        return file_name.split('.')[-1]

    def documentToText(self, file_name):
        extension = self.get_extension(file_name)
        for converter in self.converters:
            if converter.get_type() == extension:
                converter.set_path(file_name)
                return converter.convert()

if __name__ == "__main__":

    x = DocConverter()
    print x.documentToText("/Volumes/D/CViA/cv/LinkedIn/YaminiBhaskar.pdf")
