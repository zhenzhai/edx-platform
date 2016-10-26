# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob3_Part1:
	"""
	Author: Vrushali Samant
	Date: 10/24/2016
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		return "Is the spread of the normal component 1. narrow; 2. average; 3. wide? (Enter the number corresponding to the correct answer).", "1."

	def get_problems(self):
		self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_uni"]
		return self.problem_list
