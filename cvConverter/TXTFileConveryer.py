from cvConverter.BaseConverter import BaseConverter
import docx

__author__ = 'siwei'

class TXTFileConverter(BaseConverter):

    def __init__(self):
        self.type = "txt"

    def convert(self):
        return self.text+open(self.path).read()