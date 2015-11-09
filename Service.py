from Controller import Controller
from train_classifier import train
import pprint
__author__ = 'siwei'

controller = Controller()
controller.setup_evaluators()

def input_requirement(requirement):
    controller.setup_requirement(requirement)

def input_weight(weight):
    controller.set_weight(weight)

def input_job_function(job_function):
    "123"

def evaluate_cvs(cvs):
    print "evaluating CVs..."
    controller.evaluate(cvs)
    return controller.get_scores()

def tran_classifier():
    train()


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
            'must': ['r'],
            'good': []
        },
        'other':['reading']
    }

    cvs = ["cv/simple.doc",
        "cv/LinkedIn/YaminiBhaskar.pdf",
        "cv/LinkedIn/DonnabelleEmbodo.pdf",
        "cv/LinkedIn/PraveenDeorani.pdf",
        "cv/LinkedIn/RussellOng.pdf",
        "cv/LinkedIn/YaminiBhaskar.pdf"]

    input_requirement(requirement)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(evaluate_cvs(cvs))