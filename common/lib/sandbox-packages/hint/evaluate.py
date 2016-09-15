import cluster_functions
def evaluate(ans, att):
	ans = ans.strip("\[")
  	ans = ans.strip("\]")
  	ans = ans.replace("{","")
  	ans = ans.replace("}","")
  	att = att.strip("'")
	p = cluster_functions.make_params(ans, att)
	if p == {}:
		return False
	final_pairs = cluster_functions.find_matches(p)
	if len(final_pairs) == 1 and final_pairs[0][0] == 'R':
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

def test():
	print evaluate('\[0\]', '0')

test()