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


cvs = [{
    'skill':['web','android', 'ios', 'javascript'],
    'education':{
        'degree': ['master','phd'],
        'university':[]
    },
    'language':['English','Chinese']
},{
    'skill':['html','asp.net','azure'],
    'education':['bachelor'],
    'language':['English']
}]

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
x = Evaluator.Evaluator()
'''
x.setCVs(cvs)
x.setRequirement(requirement)
x.evaluate()
x.printRank()
'''

converter = Converter.DocConverter()
P = Parser()

L = LangEvaluator()
S = SkillEvaluator()
E = EduEvaluator()
EX = ExpEvaluator()
OT = OtherEvaluator()
x.add(L)
x.add(S)
x.add(E)
x.add(EX)
x.add(OT)

x.set_requirement(requirement)


cvs = ["cv/simple.doc",
        "cv/LinkedIn/YaminiBhaskar.pdf",
        "cv/LinkedIn/DonnabelleEmbodo.pdf",
        "cv/LinkedIn/PraveenDeorani.pdf",
        "cv/LinkedIn/RussellOng.pdf",
        "cv/LinkedIn/YaminiBhaskar.pdf"]

pp = pprint.PrettyPrinter(indent=4)

cv_list = []
cv_scores = []

for cv in cvs:
    CV_Text = converter.documentToText(cv)
    #print CV_Text
    cvobj = P.convertToObj(CV_Text)
    #pp.pprint(cvobj)
    cv_list.append(cvobj)
    x.set_cv(cvobj)
    cv_scores.append(x.evaluate())
    #x.print_rank()


#pp.pprint(cv_scores)
scorer = Scorer()
pp.pprint(scorer.cal_all_score(cv_scores))