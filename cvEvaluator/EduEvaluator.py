from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class EduEvaluator(BaseEvaluator):

    def __init__(self):
        self.name = "education"

    def evaluate(self, req, cv):
        req_edu = req[self.name]
        cv_edu = cv[self.name]
        edu_score = 0
        if req_edu == [] or cv_edu == []:
            return edu_score
        # print "req "+req[0]+"   has"+str(cv)
        uni_list = []
        with open('university.txt') as f:
            content = f.readlines()
            for n in range(0, len(content)):
                uni = content[n][:-1].lower()
                uni_list.append(uni)
        # print uni_list

        for eduItem in cv_edu:
            # check degree requirement
            if req_edu[0] in eduItem['degree'].lower():
                edu_score += 20
            # check university ranking
            if eduItem['university'].lower() in uni_list:
                edu_score += 5
        self.score = edu_score