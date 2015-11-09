from cvClassifier.Classifier import Classifier
from cvConverter import Converter
from cvParser.Parser import Parser
import os

__author__ = 'siwei'

root_dir_path = os.path.dirname(os.path.abspath(__file__))

converter = Converter.DocConverter()
parser = Parser()

cl = Classifier()
cl.load()

to_classify = ["cv/simple.doc"]
classified_cv = []
for cv in to_classify:
    CV_Text = converter.documentToText(root_dir_path+"/"+cv)
    cvobj = parser.convertToObj(CV_Text)
    classified_cv.append((cv, cl.classify(cvobj)))

print classified_cv