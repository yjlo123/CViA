from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class OtherEvaluator(BaseEvaluator):

    def __init__(self):
        BaseEvaluator.__init__(self)
        self.name = "other"

    def evaluate(self, req, cv):
        req_other = req[self.name]
        if req_other == [] or cv == []:
            return 0
        other_score = 0
        base_score = 2
        for s in req_other:
            s = s.lower()
            if len(cv['interest']) > 0:
                if s in (i.lower() for i in cv['interest']):
                    other_score += base_score
            if len(cv['project']) > 0:
                for proj in cv['project']:
                    if s in proj['title'].lower():
                       other_score += base_score

            if len(cv['project']) > 0:
                for proj in cv['project']:
                    if s.lower() in proj['title'].lower() or s.lower() in proj['description'].lower():
                       other_score += base_score

            # if s in cvOther['publications'].lower():
            #    other_score += base_score
            if s in cv['summary'].lower():
                other_score += base_score
        #self.score = other_score
        return other_score