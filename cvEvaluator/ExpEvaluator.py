from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class ExpEvaluator(BaseEvaluator):

    def __init__(self):
        BaseEvaluator.__init__(self)
        self.name = "experience"

    def evaluate(self, req, cv):
        req_exp = req[self.name]
        cv_exp = cv[self.name]
        exp_score = 0
        if req_exp == [] or cv_exp == []:
            return exp_score
        for pri in req_exp:
            req_exp_list = req_exp[pri]
            if pri == 'must':
                base_score = 5
            else:
                base_score = 2
            for exp in cv_exp:
                for s in req_exp_list:
                    if s.lower() in exp['title'].lower():
                        exp_score += base_score
        self.score = exp_score