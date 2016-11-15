class Prob3_Part2:
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
                hint = 'In order to calculate P(X=k), you need to know the rate parameter and k.'

            if len(hint) > 0:
                return hint + 'If you want to calculate the probability that your square will receive ' \
                              'exactly 10 hits in 24 hours, what is the value of k you should use? ', '10'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExponentialPoisson/poisson_zz/part2"]
        return self.problem_list