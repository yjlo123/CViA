from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class SkillEvaluator(BaseEvaluator):

    def __init__(self):
        BaseEvaluator.__init__(self)
        self.name = "skill"

    def evaluate(self, req, cv):
        req_skill = req[self.name]
        cv_skill = cv[self.name]
        if req_skill == [] or cv_skill == []:
            return 0
        skill_score = 0
        for pri in req_skill:
            skill_list = req_skill[pri]
            if pri == 'must':
                base_score = 5
            else:
                base_score = 2
            #print "=============="
            #print skill_list
            #print cv_skill
            for s in skill_list:
                if s.lower() in (skill.lower() for skill in cv_skill):
                    skill_score += base_score
                    #print "++++++ "+s+" "+str(base_score)
        #self.score = skill_score
        return skill_score