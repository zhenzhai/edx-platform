from hint.hint_class_helpers.get_numerical_answer import get_numerical_answer

def check_attempt(p):
	att = get_numerical_answer(p['att_tree'])
	ans = get_numerical_answer(p['ans_tree'])

	if att * ans < 0:
		return "Can the answer be negative?"
	return ""