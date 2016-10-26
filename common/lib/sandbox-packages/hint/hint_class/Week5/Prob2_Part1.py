class Prob2_Part1:
    """
    Author: Geovonni Najera
    Date: 10/25/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        

        hint = 'Recall how standard deviation relates to the distribution of a normal distribution.'
        
        return hint + ' How many lengths of std would cover approximately 99.7% of the distribution?', '3'

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_point/part1"]
        return self.problem_list
