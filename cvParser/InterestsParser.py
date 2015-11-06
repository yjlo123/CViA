import FieldFactory
__author__ = 'haojiang'



class InterestParser:

    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseInterest(self,text):
        textList = text.split(",")
        return self.factory.produce("interest",textList)
