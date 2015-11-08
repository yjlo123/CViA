import pprint

__author__ = 'siwei'


class Evaluator:

    def __init__(self):
        self.cvList = []
        self.requirement = {}
        self.scoreList = []
        self.evaluators = []

    def set_cvs(self, cvs):
        self.cvList = cvs

    def set_requirement(self, req):
        self.requirement = req

    def add(self, eva):
        self.evaluators.append(eva)

    def evaluate(self):
        for cv in self.cvList:
            this_score = {}
            for eva in self.evaluators:
                eva_name = eva.get_name()
                this_score[eva_name] = eva.evaluate(self.requirement, cv)
            self.scoreList.append({'score': this_score, 'cv': cv})

    def print_rank(self):
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.scoreList)
        to_print = ""
        for e in self.evaluators:
            to_print += e.to_string()
        #pp.pprint(self.cvList[0])
        pp.pprint(to_print)


if __name__ == "__main__":
    print ""
