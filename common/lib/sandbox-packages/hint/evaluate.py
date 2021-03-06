from hint_class_helpers.make_params import make_params
from hint_class_helpers.get_numerical_answer import get_numerical_answer
from hint_class_helpers.find_matches import find_matches
from hint_class_helpers.find_matches_w_variables import find_matches_w_variables

def check_w_tol(ans, att, tol):
	if ans == 0:
		if att == 0:
			return True
		else:
			return False
	else:
		ratio = float(att)/ans
		if ratio < tol and ratio > (1/tol):
			return True
		else:
			return False


def evaluate(ans, att, tol = 1+1e-5):
	ans = ans.strip("\[")
  	ans = ans.strip("\]")
  	ans = ans.replace("{","")
  	ans = ans.replace("}","")
  	att = att.strip("'")
  	#logger.info("evaluating attempt: {0}, answer: {1}.".format(att, ans))
	p = make_params(ans, att)
	if p == {}:
		#logger.info("param empty from evaluate")
		return False
	att_value = get_numerical_answer(p['att_tree'])
	ans_value = get_numerical_answer(p['ans_tree'])
	final_pairs = find_matches(p, tol)
	#logger.info("output matching: {0}.".format(final_pairs))

	if len(final_pairs) == 1 and final_pairs[0][0] == 'R':
		return True
	elif check_w_tol(ans_value, att_value, tol):
		return True
	else:
		return False


def evaluate_w_variables(ans, att, variable_values, test_all=False):
	ans = ans.strip("\[")
  	ans = ans.strip("\]")
  	ans = ans.replace("{","")
  	ans = ans.replace("}","")
  	att = att.strip("'")
	matches = find_matches_w_variables(ans, att, variable_values, test_all)
	if matches and len(matches) == 1 and matches[0][0] == 'R':
		return True
	else:
		return False