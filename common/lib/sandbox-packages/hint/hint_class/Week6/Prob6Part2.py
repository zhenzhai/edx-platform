class Prob6_Part2:
	"""
	Author: Sunil Raiyani
	Date: 10/31/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		#print self.answer[7]
		hint=''
		
		try:
			if '0.5' not in self.attempt and '1/2' not in self.attempt:
				hint='You are concerned with only half part of the probability in Chebyshev\'s equation now i.e P(X-E[X]>=a) (without the modulus) How will it affect your equation?'
			
			if len(hint)>0:
                                return hint+' If P(|X|>=a) <= 0.6 and the distribution is symmetric around 0, what is P(X>=a)?','0.3'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["MarkovChebyshev/chebyshev/part2"]
		return self.problem_list
