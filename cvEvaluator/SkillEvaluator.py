from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class SkillEvaluator(BaseEvaluator):

    def __init__(self):
        self.name = "skill"

    def evaluate(self, req, cv):
        req_skill = req[self.name]
        cv_skill = cv[self.name]
        if req_skill == [] or cv_skill == []:
            return 0
        this_score = 0
        for pri in req_skill:
            skill_list = req_skill[pri]
            if pri == 'must':
                base_score = 5
            else:
                base_score = 2
            for s in skill_list:
                if s in cv_skill:
                    this_score += base_score
        self.score = this_score