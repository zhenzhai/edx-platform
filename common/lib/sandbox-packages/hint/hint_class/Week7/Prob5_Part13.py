# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches

class Prob5_Part13:
    """
    Author: Shen Ting Ang
    Date: 11/7/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            hint = 'Recall how to find the correlation coefficient between X and Y.'
            return hint + ' If Cov(X,Y) is 4, sqrt(Var(X)) is 2 and sqrt(Var(Y)) is 2, what is the correlation coefficient between X and Y?', '1'

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["ExpectationVariance/cov_dep_corr.imd"]
        return self.problem_list