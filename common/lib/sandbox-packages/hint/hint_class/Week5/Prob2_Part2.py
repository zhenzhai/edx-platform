class Prob2_Part2:
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

        

        hint = 'Recall notes on mixtures.'
        
        return hint + ' If B(x) was a PDF over the interval [0,3] and it had a componment weight of 7, what would the CDF be at x=3', '7'

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_point/part2"]
        return self.problem_list
