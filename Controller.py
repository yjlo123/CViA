from cvConverter import Converter
from cvEvaluator.EduEvaluator import EduEvaluator
from cvEvaluator.ExpEvaluator import ExpEvaluator
from cvEvaluator.LangEvaluator import LangEvaluator
from cvEvaluator.OtherEvaluator import OtherEvaluator
from cvEvaluator.SkillEvaluator import SkillEvaluator
from cvParser.Parser import Parser
from cvEvaluator import Evaluator
import pprint
from cvScorer.Scorer import Scorer

__author__ = 'siwei'

class Controller():
    def __init__(self):
        self.evaluator = Evaluator.Evaluator()
        self.parser = Parser()
        self.converter = Converter.DocConverter()
        self.scorer = Scorer()
        self.cv_list = []
        self.cv_scores = []

    def setup_evaluators(self):
        language_evaluator = LangEvaluator()
        skill_evaluator = SkillEvaluator()
        education_evaluator = EduEvaluator()
        experience_evaluator = ExpEvaluator()
        other_evaluator = OtherEvaluator()
        self.evaluator.add(language_evaluator)
        self.evaluator.add(skill_evaluator)
        self.evaluator.add(education_evaluator)
        self.evaluator.add(experience_evaluator)
        self.evaluator.add(other_evaluator)

    def setup_requirement(self, requirement):
        self.evaluator.set_requirement(requirement)

    def evaluate(self, cvs):
        for cv in cvs:
            CV_Text = self.converter.documentToText(cv)
            #print CV_Text
            cvobj = self.parser.convertToObj(CV_Text)
            #pp.pprint(cvobj)
            self.cv_list.append(cvobj)
            self.evaluator.set_cv(cvobj)
            self.cv_scores.append(self.evaluator.evaluate())
            #x.print_rank()

    def get_scores(self):
        return self.scorer.cal_all_score(self.cv_scores)

    def get_cv_list(self):
        return self.cv_list

    def get_cv_score(self):
        return self.cv_scores


if __name__ == "__main__":
    requirement = {
        'education':['bachelor'],
        'skill': {
            'must': ['windows','vpn','Web Development'],
            'good': ['xp','iOS']
        },
        'language':{
            'must': ['English'],
            'good': ['Chinese']
        },
        'experience':{
            'must': ['engineer'],
            'good': []
        },
        'other':['Google','reading']
    }

    cvs = ["cv/simple.doc",
        "cv/LinkedIn/YaminiBhaskar.pdf",
        "cv/LinkedIn/DonnabelleEmbodo.pdf",
        "cv/LinkedIn/PraveenDeorani.pdf",
        "cv/LinkedIn/RussellOng.pdf",
        "cv/LinkedIn/YaminiBhaskar.pdf"]

    pp = pprint.PrettyPrinter(indent=4)

    ctrl = Controller()
    ctrl.setup_evaluators()
    ctrl.setup_requirement(requirement)
    ctrl.evaluate(cvs)
    pp.pprint(ctrl.get_cv_score())