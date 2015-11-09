from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import stopwords
import pickle
import os
# download nltk corpus: python -m textblob.download_corpora

__author__ = 'siwei'

class Classifier:
    def __init__(self):
        self.cachedStopWords = stopwords.words("english")
        self.path = os.path.dirname(os.path.abspath(__file__))

    def train(self, train_set):
        train_data = []
        for t in train_set:
            train_data.append((self._cvobj_to_string(t[0]),t[1]))
        print "Training model..."
        #print train_data
        self.cl = NaiveBayesClassifier(train_data)
        #print self._cvobj_to_string(train_set[0][0])

    def _cvobj_to_string(self, cv):
        str = ""
        for exp in cv['experience']:
            str += (exp['description']+" ")
        for proj in cv['project']:
            str += (proj['title']+" ")
            str += (proj['description']+" ")
        for skill in cv['skill']:
            str += (skill+" ")
        str = str.decode("utf-8", "replace")
        str = ' '.join([word for word in str.split() if word not in self.cachedStopWords])
        return str

    def classify(self, cv):
        return self.cl.classify(self._cvobj_to_string(cv))

    def save(self):
        pickle.dump( self.cl, open( self.path+"/cv_model.cvm", "wb" ) )
        print "CV classifier saved."

    def load(self):
        self.cl = pickle.load( open( self.path+"/cv_model.cvm", "rb" ) )
        print "CV classifier loaded."