import cluster_functions
def evaluate(ans, att):
	p = cluster_functions.make_params(ans, att)
	if param == {}:
      return False
	final_pairs = cluster_functions.find_matches(p)
	if len(final_pairs) == 1 and final_pairs[0][0] == 'R':
		return True
	return False

def evaluate_w_variables(ans, att, variable_values, test_all=False):
	matches = cluster_functions.show_matching_group_w_variables(ans, att, variable_values, test_all)
	if len(matches) == 1 and matches[0] == att:
		return True
	return False


    