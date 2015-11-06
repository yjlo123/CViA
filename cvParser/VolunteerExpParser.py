
import re
import FieldFactory

__author__ = 'haojiang'


class VolunteerExpParser:
    def __init__(self):
        self.factory = FieldFactory.FieldFacory()

    def ParseVolunteerExp(self,ExpStr):
        VolunteerExpList = ExpStr.splitlines()
        dateArr = []
        result = []
        for i in range(0,len(VolunteerExpList)):
            if self.MatchExpDate(VolunteerExpList[i]):
                dateArr.append(i)
        for i in range(0,len(dateArr)):
            index = dateArr[i]
            if i != len(dateArr)-1:
                title = VolunteerExpList[index-1]
                period = VolunteerExpList[index].split("(")[1][:len(VolunteerExpList[index].split("(")[1])-1]
                description = ""

                ### Not EMPTY description ###
                if index+3 != dateArr[i+1]:
                    temp = index+2
                    end = dateArr[i+1]-1
                    while(temp!=end):
                        description = description + VolunteerExpList[temp]
                        temp+=1

            else:
                title = VolunteerExpList[index-1]
                period = VolunteerExpList[index].split("(")[1][:len(VolunteerExpList[index].split("(")[1])-1]
                description =""

                ### Not EMPTY description
                if index+1 != len(VolunteerExpList):
                    temp=index+2
                    end = len(VolunteerExpList)
                    while(temp!=end):
                        description = description + VolunteerExpList[temp]
                        temp+=1
            result.append(self.factory.produce("volunteerexp",title,period,description))
        return result

    def MatchExpDate(self,text):  # <--- Check whether the string is a date string
        if len(text.split("("))>1 and len(text)<50 and "-" in text:
        # From " May 2013 - May 2015 (2 years)" extract date.
            first = text.split("(")[0].split("-")[0]
            second = text.split("(")[0].split("-")[1]
            return re.findall(r'(?:january|february|march|april|may|june|july|august|september|october|november|december)\s\d{4}', first) !=[] and \
                   (re.findall(r'(?:january|february|march|april|may|june|july|august|september|october|november|december)\s\d{4}', second) !=[] or second =="  present ")
        else:
            return False