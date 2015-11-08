from cvEvaluator.BaseEvaluator import BaseEvaluator

__author__ = 'siwei'

class LangEvaluator(BaseEvaluator):

    def __init__(self):
        BaseEvaluator.__init__(self)
        self.name = "language"

    def evaluate(self, req, cv):
        req_lang = req[self.name]
        cv_lang = cv[self.name]
        if req_lang == [] or cv_lang == []:
            return 0
        this_score = 0
        for pri in req_lang:
            lang_list = req_lang[pri]
            if pri == 'must':
                base_score = 5
            else:
                base_score = 2
            for s in lang_list:
                if s in cv_lang:
                    this_score += base_score
        self.score = this_score
