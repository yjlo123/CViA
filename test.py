from cvConverter import Converter
from cvEvaluator.EduEvaluator import EduEvaluator
from cvEvaluator.ExpEvaluator import ExpEvaluator
from cvEvaluator.LangEvaluator import LangEvaluator
from cvEvaluator.OtherEvaluator import OtherEvaluator
from cvEvaluator.SkillEvaluator import SkillEvaluator
from cvParser.Parser import Parser
from cvEvaluator import Evaluator
import pprint

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

for cv in cvs:
    CV_Text = converter.documentToText(cv)
    cvobj = P.convertToObj(CV_Text)
    x.set_cvs([cvobj])
    x.evaluate()
    x.print_rank()