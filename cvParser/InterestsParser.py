import FieldFactory
__author__ = 'haojiang'



class InterestParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseInterest(self,text):
        textList = text.split(",")
        for i in range(0,len(textList)):
            textList[i] = textList[i].strip()
        return self.factory.produce("interest",textList)
