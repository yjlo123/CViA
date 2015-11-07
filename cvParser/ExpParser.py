
import re
import FieldFactory

__author__ = 'haojiang'


class ExpParser:
    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseExp(self,ExpStr):
        ExpList = ExpStr.splitlines()
        dateArr = []
        result = []
        for i in range(0,len(ExpList)):
            if self.MatchExpDate(ExpList[i]):
                dateArr.append(i)
        for i in range(0,len(dateArr)):
            index = dateArr[i]
            if i != len(dateArr)-1:
                title = ExpList[index-1]
                period = ExpList[index].split("(")[1][:len(ExpList[index].split("(")[1])-1]
                description = ""

                ### Not EMPTY description ###
                if index+3 != dateArr[i+1]:
                    temp = index+2
                    end = dateArr[i+1]-1
                    while(temp!=end):
                        description = description + ExpList[temp]
                        temp+=1

            else:
                title = ExpList[index-1]
                period = ExpList[index].split("(")[1][:len(ExpList[index].split("(")[1])-1]
                description =""

                ### Not EMPTY description
                if index+1 != len(ExpList):
                    temp=index+2
                    end = len(ExpList)
                    while(temp!=end):
                        description = description + ExpList[temp]
                        temp+=1
            result.append(self.factory.produce("exp",title,period,description))
        return result

    def MatchExpDate(self,text):  # <--- Check whether the string is a date string
        if len(text.split("("))>1 and len(text)<50 and "-" in text:
        # From " May 2013 - May 2015 (2 years)" extract date.
            first = text.split("(")[0].split("-")[0].strip()
            second = text.split("(")[0].split("-")[1].strip()
            return re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}', first) !=[] and \
                   (re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}', second) !=[] or second =="Present")
        else:
            return False