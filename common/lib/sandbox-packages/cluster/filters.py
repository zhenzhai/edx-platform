import cluster_functions

def universal_hint(p):
    if len(p['att_tree']) > 1:
        if p['att_tree'][0] == 'X':
            att = p['att_tree'][1]
        else:
            att = p['att_tree'][0][1]
        if p['ans_tree'][0] == 'X':
            ans = p['ans_tree'][1]
        else:
            ans = p['ans_tree'][0][1]
        if att * ans < 0:
            return hint_wrong_sign()
        elif float(ans).is_integer() and not float(att).is_integer():
            return hint_fraction()
        elif p['ans_tree'][0] == 'X' and p['att_tree'][0] != 'X':
            return hint_numerial()


def hint_wrong_sign():
	return "Please double check your answer to make sure your sign is correct."

def hint_fraction():
	return "Please double check your answer to make sure it is an integer."

def hint_numerical():
	return "Please write an expression instead of a number."