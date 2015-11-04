import FieldFactory
from CVFields import LanguageField
__author__ = 'haojiang'



class SkillParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseSkill(self,text):
        textList = text.splitlines()
        breakPoint = len(textList)
        for i in range(0,len(textList)-1):
            if textList[i] == "":
                breakPoint = i 
        textList = textList[:breakPoint]
        print textList
        return LanguageField.LanguageField(textList).__dict__["Language"]
