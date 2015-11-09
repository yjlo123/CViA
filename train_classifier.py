from cvClassifier.Classifier import Classifier
from cvConverter import Converter
from cvParser.Parser import Parser
import pprint
import os

__author__ = 'siwei'

root_dir_path = os.path.dirname(os.path.abspath(__file__))

cvs = [("cv/LinkedIn/YaminiBhaskar.pdf","2"),
        ("cv/LinkedIn/DonnabelleEmbodo.pdf","3"),
        ("cv/LinkedIn/PraveenDeorani.pdf","4"),
        ("cv/LinkedIn/RussellOng.pdf","5"),
        ("cv/LinkedIn/YaminiBhaskar.pdf","6")]

train_data = []

def train():
    print "Converting CV files ..."
    converter = Converter.DocConverter()
    parser = Parser()
    print "Parsing CVs..."
    for cv in cvs:
        CV_Text = converter.documentToText(root_dir_path+"/"+cv[0])
        cvobj = parser.convertToObj(CV_Text)
        train_data.append((cvobj, cv[1]))


    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(train_data)

    cl = Classifier()
    cl.train(train_data)
    cl.save()