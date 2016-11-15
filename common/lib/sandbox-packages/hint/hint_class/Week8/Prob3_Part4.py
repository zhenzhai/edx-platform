class Prob3_Part4:
    """
    Author: Liu Han
    Date: 11/14/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            if not '/' in self.attempt:
                hint = 'Suppose you want to calculate the probability that the time between consecutive ' \
                       'hits will be shorter than 1 hours.'

            if len(hint) > 0:
                return hint + 'What is the time difference between two consecutive bombs?', '1/24'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/poisson_zz/part4"]
        return self.problem_list