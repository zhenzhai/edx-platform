class Prob4_Part1:
    """
    Author: Chang Qiu
    Date: 10/25/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        return "Component weights take on multiples of 0.05 and the exponential component is 1, what's the component weight?", "0.95"

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_point/part1"]
        return self.problem_list