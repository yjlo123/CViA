from cvEvaluator.EduEvaluator import EduEvaluator
from cvEvaluator.ExpEvaluator import ExpEvaluator
from cvEvaluator.LangEvaluator import LangEvaluator
from cvEvaluator.OtherEvaluator import OtherEvaluator
from cvEvaluator.SkillEvaluator import SkillEvaluator
import doc_converter
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
        'good': ['xp']
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

converter = doc_converter.DocConverter()
#CV_Text = converter.documentToText("cv/simple.doc")
CV_Text = converter.documentToText("cv/LinkedIn/DesmondLim.pdf")
#print CV_Text
P = Parser()
cvobj = P.convertToObj(CV_Text)
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(cvobj)
x.set_cvs([cvobj])
x.set_requirement(requirement)

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

x.evaluate()
x.print_rank()