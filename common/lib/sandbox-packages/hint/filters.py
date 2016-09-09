import cluster_functions
from xml.sax.saxutils import escape

def hint_wrong_sign():
	return "Can the number of strings satisfying the constraint be negative?"

def hint_fraction():
	return "Can the number of strings satisfying the constraint be fractional?"

def hint_numerical():
	return "Your answer is incorrect, please write an expression."

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
        elif p['att_tree'][0] == 'X' and p['ans_tree'][0] != 'X':
            return hint_numerical()
        else:
            return ""

def universal_hint_w_variables(p, variables):
    """
    input variables should be a list of strings of variable names 
    """
    for v in variables:
        if not v in p['attempt']:
            return "Your answer should include variable " + v