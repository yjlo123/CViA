import FieldFactory
from CVFields import LanguageField
__author__ = 'haojiang'



class LanguageParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseLanguage(self,text):
        textList = text.splitlines()
        breakPoint = len(textList)
        for i in range(0,len(textList)-1):
            if textList[i] == "":
                breakPoint = i
        textList = textList[:breakPoint]
        return LanguageField.LanguageField(textList).__dict__["Language"]

