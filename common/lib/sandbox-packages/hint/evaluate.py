from hint_class_helpers.make_params import make_params
from hint_class_helpers.get_numerical_answer import get_numerical_answer
from hint_class_helpers.find_matches import find_matches
from hint_class_helpers.find_matches_w_variables import find_matches_w_variables


"""import logging.handlers
import logging
# logging settings
log_path = 'evaluate.log'
logger = logging.getLogger('evaluate')
handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 16)
formatter = logging.Formatter('%(asctime)s - %(name)s: EVAL %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)"""

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
	p = make_params(ans, att)
	if p == {}:
		#logger.info("param empty from evaluate")
		return False
	att_value = get_numerical_answer(p['att_tree'])
	ans_value = get_numerical_answer(p['ans_tree'])
	final_pairs = find_matches(p)

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
	matches = find_matches_w_variables(ans, att, variable_values, test_all)
	if matches and len(matches) == 1 and matches[0] == att:
		return True
	else:
		return False