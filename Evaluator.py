import doc_converter

__author__ = 'siwei'

import pprint
from cvParser.Parser import Parser
import unicodedata

class Evaluator:

    def __init__(self):
        self.cvList = []
        self.requirement = {}
        self.scoreList = []

    def setCVs(self, cvs):
        self.cvList = cvs

    def setRequirement(self, req):
        self.requirement = req

    def evaluate(self):
        for cv in self.cvList:
            thisScore = {'language':0}
            for req in self.requirement:
                if req == 'education':
                    thisScore['education'] = self.evaluateEducation(self.requirement[req], cv[req])
                elif req == 'skill':
                    thisScore['skill'] = self.evaluateSkill(self.requirement[req], cv[req])
                elif req == 'language':
                    thisScore['language'] = self.evaluateLanguage(self.requirement[req], cv[req])
                elif req == 'experience':
                    thisScore['experience'] = 0
                else:
                    thisScore['other'] = 0
            self.scoreList.append({'score':thisScore,'cv':cv})

    def evaluateEducation(self, reqEdu, cvEdu):
        eduScore = 0
        if reqEdu == [] or cvEdu == []:
            return eduScore
        #print "req "+req[0]+"   has"+str(cv)
        uniList = []
        with open('university.txt') as f:
            content = f.readlines()
            for n in range(0, len(content)):
                uni = content[n][:-1].lower()
                uniList.append(uni)
        #print uni_list

        for eduItem in cvEdu:
            # check degree requirement
            if reqEdu[0] in eduItem['degree']:
                eduScore += 20
            # check university ranking
            if eduItem['university'] in uniList:
                eduScore += 5
        return eduScore

    def evaluateSkill(self, req, cv):
        if req == [] or cv == []:
            return 0
        thisScore = 0
        for type in req:
            skillList = req[type]
            if type == 'must':
                baseScore = 5
            else:
                baseScore = 2
            for s in skillList:
                if s in cv:
                    thisScore += baseScore
        return thisScore

    def evaluateLanguage(self, req, cv):
        if req == [] or cv == []:
            return 0
        thisScore = 0
        for type in req:
            skillList = req[type]
            if type == 'must':
                baseScore = 5
            else:
                baseScore = 2
            for s in skillList:
                if s in cv:
                    thisScore += baseScore
        return thisScore

    def printRank(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.scoreList)


if __name__ == "__main__":
    cvs = [{
        'skill':['web','android', 'ios', 'javascript'],
        'education':{
            'degree': ['master','phd'],
            'university':[]
        },
        'language':['English','Chinese']
    },{
        'skill':['html','asp.net','azure'],
        'education':['bachelor'],
        'language':['English']
    }]

    requirement = {
        'education':['bachelor'],
        'skill': {
            'must': ['windows','vpn','web development'],
            'good': ['xp']
        },
        'language':{
            'must': ['english'],
            'good': ['chinese']
        }
    }
    x = Evaluator()
    '''
    x.setCVs(cvs)
    x.setRequirement(requirement)
    x.evaluate()
    x.printRank()
    '''

    converter = doc_converter.DocConverter()
    #CV_Text = converter.documentToText("cv/simple.doc")
    CV_Text = converter.documentToText("cv/DesmondLim.pdf")
    #print CV_Text
    P = Parser()
    cvobj = P.convertToObj(CV_Text)

    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(cvobj)
    x.setCVs([cvobj])
    x.setRequirement(requirement)
    x.evaluate()
    x.printRank()
