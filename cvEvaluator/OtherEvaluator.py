from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class OtherEvaluator(BaseEvaluator):

    def __init__(self):
        self.name = "other"

    def evaluate(self, req, cv):
        req_other = req[self.name]
        if req_other == [] or cv == []:
            return 0
        this_score = 0
        base_score = 2
        for s in req_other:
            s = s.lower()
            if not cv['interest']:
                if s in cv['interest'].lower():
                    this_score += base_score
            if len(cv['project']) > 0:
                for proj in cv['project']:
                    if s in proj['title'].lower():
                       this_score += base_score
            '''
            if len(cvOther['project']) > 0:
                for proj in cvOther['project']:
                    if s in proj['title'].lower():
                       this_score += base_score
            '''
            # if s in cvOther['publications'].lower():
            #    this_score += base_score
            if s in cv['summary'].lower():
                this_score += base_score
        self.score = this_score