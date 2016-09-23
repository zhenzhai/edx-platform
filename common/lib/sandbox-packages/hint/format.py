import logging.handlers


# logging settings
log_path = 'hint_format.log'
logger = logging.getLogger('hint.format')
handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 16)
formatter = logging.Formatter('%(asctime)s: FORMAT %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def format_u_hint(hint_text, hint_id, i):
	'''
		input: hint text in string, hint ids in list, part index
		output: formated hint with "show hint" button
	'''
	if i >= len(hint_id):
		logger.error("index out of range in foramt_u_hint")
		return ""

	textHint_id = hint_id[i] + "_textHint"
	hintDiv_id = hint_id[i] + "_hintDiv"
	hint_text = "<font color='grey'>Hint: {0}</font>".format(hint_text)

	hint = "<div stype='display:none' id='{0}'>".format(hintDiv_id)
	hint += "<div style='padding:10px 10px 10px 0px;'>"
	hint += "<button onclick='show_textHint_in_problem({0})'>Show hint</button>".format(i)
	hint += "<p id='{0}' style='display:none'> {1} </p>".format(textHint_id, hint_text)
	hint += "</div></div>"
	return hint

def format_c_hint(hint_text, hint_id, hint_answer, i):
	'''
		input: hint text in string, hint ids in list,
			   hint answer in string, part index
		output: formated hint with "show hint" button
	'''
	if i >= len(hint_id):
		logger.error("index out of range in foramt_c_hint")
		return ""

	hintDiv_id = hint_id[i] + "_hintDiv"
	hint_answer_id = hint_id[i] + "answer"

	hint = "<div stype='display:none' id='{0}'>".format(hintDiv_id)
	hint += "<div style='padding:10px 10px 10px 0px;'>"
	hint += "<button onclick='show_hint_in_problem({0})'>Show hint</button>".format(i)
	hint += "<p id='{0}' style='display:none'> {1} </p>".format(hint_id[i], hint_text)
	hint += "<p id='{0}' style='display:none'> {1} </p>".format(hint_answer_id, hint_answer)
	hint += "</div></div>"
	return hint