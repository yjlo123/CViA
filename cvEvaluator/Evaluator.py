import pprint

__author__ = 'siwei'


class Evaluator:

    def __init__(self):
        self.cv = {}
        self.requirement = {}
        self.scored_cv = {}
        self.evaluators = []

    def set_cv(self, cv):
        self.cv = cv

    def set_requirement(self, req):
        self.requirement = req

    def add(self, eva):
        self.evaluators.append(eva)

    def evaluate(self):
        this_score = {}
        for eva in self.evaluators:
            eva_name = eva.get_name()
            this_score[eva_name] = eva.evaluate(self.requirement, self.cv)
        self.scored_cv = {'cv': self.cv['path'], 'score': this_score}
        return self.scored_cv

    def print_rank(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.scored_cv)


if __name__ == "__main__":
    print ""
