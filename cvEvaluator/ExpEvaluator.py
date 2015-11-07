from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class ExpEvaluator(BaseEvaluator):

    def __init__(self):
        self.name = "experience"

    def evaluate(self, req, cv):
        req_exp = req[self.name]
        cv_exp = cv[self.name]
        if req_exp == [] or cv_exp == []:
            return 0
        this_score = 0
        for pri in req_exp:
            req_exp_list = req_exp[pri]
            if pri == 'must':
                base_score = 5
            else:
                base_score = 2
            for exp in cv_exp:
                for s in req_exp_list:
                    if s.lower() in exp['title'].lower():
                        this_score += base_score
        self.score = this_score