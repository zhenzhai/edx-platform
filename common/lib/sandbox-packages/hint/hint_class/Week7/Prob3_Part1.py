class Prob3_Part1:
    """
    Author: Geovonni Najera
    Date: 11/7/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            if len(hint) > 0:
                return hint + 'Try to simplify the function. Please enter 1 once done', '1'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["ExpectationVariance/Notes_3_2_1"]
        return self.problem_list