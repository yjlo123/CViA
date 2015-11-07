import FieldFactory
from CVFields import LanguageField
__author__ = 'haojiang'



class LanguageParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseLanguage(self,text):
        textList = text.splitlines()
        for i in range(0,len(textList)):
            if " " in textList[i] or "(" in textList[i] or ")" in textList[i]:
                textList[i] = ""
        textList = filter(None,textList)
        return self.factory.produce("language",textList)

