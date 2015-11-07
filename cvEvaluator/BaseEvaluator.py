__author__ = 'siwei'

class BaseEvaluator:

    def __init__(self):
        self.score = 0
        self.name = ""

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def to_string(self):
        return "["+self.get_name()+": "+str(self.get_score())+"]"
