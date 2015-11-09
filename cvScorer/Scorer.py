__author__ = 'siwei'

class Scorer:
    def __init__(self):
        self.ratio = {}

    def set_weight(self, weight):
        ratio_total = 0
        for r in weight:
            ratio_total += weight[r]
        for r in weight:
            self.ratio[r] = weight[r]*1.0/ratio_total

    def set_default_weight(self, scored_cv):
        num_field = len(scored_cv['score'])
        for f in scored_cv['score']:
            self.ratio[f] = 1.0/num_field

    def cal_score(self, scored_cv):
        total_score = 0
        scores = scored_cv['score']
        for key in scores:
            total_score += scores[key]*self.ratio[key]
        return total_score

    def cal_all_score(self, scored_cvs):
        if self.ratio == {}:
            self.set_default_weight(scored_cvs[0])
        for i in range(0, len(scored_cvs)):
            scored_cvs[i]['total'] = self.cal_score(scored_cvs[i])
        return scored_cvs