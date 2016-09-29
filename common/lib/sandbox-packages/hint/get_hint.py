from hint_class_helpers.get_universal_hints import get_first_universal_hints
from hint_class_helpers.get_universal_hints import get_last_universal_hints
from hint_class_helpers.get_conditional_hints import get_conditional_hints
from hint_class_helpers.make_params import make_params
import hint_format

def get_hint(ans, att, hint_text_id, i):
	param = make_params(ans, att)
	if param == {}:
		return ""
	hint = get_first_universal_hints(param)
	if hint:
		hint = hint_format.format_u_hint(hint, hint_text_id, i)
		return hint

	#hint_text, hint_answer = get_conditional_hints(hint_text_id, i, param)
	hint_text = ""
	if hint_text:
		hint = hint_format.format_c_hint(hint_text, hint_text_id, hint_answer, i)
		return hint

	hint = get_last_universal_hints(param)
	if hint:
		hint = hint_format.format_u_hint(hint, hint_text_id, i)
		return hint

	return ""


def get_hint_w_variables(ans, att, hint_text_id, i, variables):
	"""
	input variables should be a list of strings of variable names 
	"""
	param = make_params(ans, att)
	if param == {}:
		return ""
	return ""