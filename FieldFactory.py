__author__ = 'haojiang'

from CVFields import EducationField
from CVFields import ExperienceField

class FieldFacory:
    def __init__(self):
        self.Expresult=[]
    def produceEdu(self):
        res = EducationField.EducationField()
        attr1 = "Name"
        attr2 = "Date"
        setattr(res,attr1,"NUS")
        setattr(res,attr2,"May 2016")
        return res
    def produceExp(self,text):
        textList = text.split("|||")
        for i in range(0,len(textList)):
            currentExpArr = textList[i].split("---")
            if len(currentExpArr) == 3:
                currentExpObj = ExperienceField.ExperienceField()
                setattr(currentExpObj,"title",currentExpArr[0])
                setattr(currentExpObj,"period",currentExpArr[1])
                setattr(currentExpObj,"description",currentExpArr[2])
                Expdict = currentExpObj.__dict__
                self.Expresult.append(Expdict)
        return self.Expresult

    def produce(self,fieldName, text):
        if fieldName == "Exp":
            return self.produceExp(text)
