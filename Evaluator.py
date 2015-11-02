__author__ = 'siwei'

import pprint

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
            thisScore = 0
            for req in self.requirement:
                if req == 'education':
                    thisScore += self.evaluateEducation(self.requirement[req], cv[req])
                elif req == 'skill':
                    thisScore += self.evaluateSkill(self.requirement[req], cv[req])
                elif req == 'language':
                    thisScore += self.evaluateLanguage(self.requirement[req], cv[req])
                elif req == 'experience':
                    thisScore += 0
                else:
                    thisScore += 0
            self.scoreList.append({'score':thisScore,'cv':cv})

    def evaluateEducation(self, req, cv):
        if req == [] or cv == []:
            return 0
        #print "req "+req[0]+"   has"+str(cv)
        if req[0] in cv:
            return 20
        return 0

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
        'education':['master','phd'],
        'language':['english','chinese']
    },{
        'skill':['html','asp.net','azure'],
        'education':['bachelor'],
        'language':['english']
    }]

    requirement = {
        'education':['master'],
        'skill': {
            'must': ['android'],
            'good': []
        },
        'language':{
            'must': ['english'],
            'good': ['chinese']
        }
    }
    x = Evaluator()
    x.setCVs(cvs)
    x.setRequirement(requirement)
    x.evaluate()
    x.printRank()
