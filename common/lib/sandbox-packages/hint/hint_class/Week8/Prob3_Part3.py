class Prob3_Part3:
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
            if not '/' in self.attempt or not '*' in self.attempt or not '!' in self.attempt:
                hint = 'Assume the probability that a square will receive exactly 1 hits in 24 hours is ' \
                       '1/2, and there are total of 10 equal area squares;'

            if len(hint) > 0:
                return hint + 'What is the expected number of squares that will receive exactly 1 hits in ' \
                              '24 hours?', '5'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/poisson_zz/part3"]
        return self.problem_list