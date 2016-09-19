import cluster_functions

def check_w_tol(ans, att, tol = 1+1e-3):
	if ans == 0:
		if att == 0:
			return True
		else:
			return False
	else:
		ratio = att/ans
		if ratio < tol and ratio > (1/tol):
			return True
		else:
			return False


def evaluate(ans, att):
	ans = ans.strip("\[")
  	ans = ans.strip("\]")
  	ans = ans.replace("{","")
  	ans = ans.replace("}","")
  	att = att.strip("'")
	p = cluster_functions.make_params(ans, att)
	if p == {}:
		return False
	att_value = cluster_functions.get_numerical_answer(p['att_tree'])
	ans_value = cluster_functions.get_numerical_answer(p['ans_tree'])
	final_pairs = cluster_functions.find_matches(p)

	if len(final_pairs) == 1 and final_pairs[0][0] == 'R':
		return True
	elif check_w_tol(ans_value, att_value):
		return True
	else:
		return False

def evaluate_w_variables(ans, att, variable_values, test_all=False):
	ans = ans.strip("\[")
  	ans = ans.strip("\]")
  	ans = ans.replace("{","")
  	ans = ans.replace("}","")
  	att = att.strip("'")
	matches = cluster_functions.show_matching_group_w_variables(ans, att, variable_values, test_all)
	if matches and len(matches) == 1 and matches[0] == att:
		return True
	else:
		return False