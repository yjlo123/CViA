import FieldFactory
from CVFields import EducationField
__author__ = 'haojiang'



class EduParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseEdu(self,text):
        textList = text.splitlines()
        indexarr = []
        result = []
        for i in range(0,len(textList)):
            if self.iskeysentence(textList[i]):
                indexarr.append(i)
        for i in range(0,len(indexarr)):
            theindex = indexarr[i]
            university = textList[theindex-1].strip()
            degree = textList[theindex].split(",")[0].strip()
            major = textList[theindex].split(",")[1].strip()
            result.append(self.factory.produce("edu",university,degree,major))
        return result

    # To check whether is the "degree,major,date" or not
    def iskeysentence(self,str):
        result = False
        target = str.split(",")
        if len(target) == 3:
            if len(target[2].split())==3:
                advTarget = target[2].split()
                if advTarget[1] == '-' and advTarget[0].isdigit() and advTarget[2].isdigit():
                    result = True
        return result