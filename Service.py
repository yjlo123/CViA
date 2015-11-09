from Controller import Controller
from train_classifier import train

__author__ = 'siwei'

controller = Controller()

def init():
    controller.setup_evaluators()

def input_requirement(requirement):
    controller.setup_requirement(requirement)

def evaluate_cvs(cvs):
    print "evaluating CVs..."
    controller.evaluate(cvs)
    return controller.get_cv_score()

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

    init()
    input_requirement(requirement)
    print evaluate_cvs(cvs)