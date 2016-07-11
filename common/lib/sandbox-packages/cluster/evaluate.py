import cluster_functions
def evaluate(p):
	final_pairs = cluster_functions.find_matches(p)
	if len(final_pairs) == 1 and final_pairs[0][0] == ['R']:
		return True
    