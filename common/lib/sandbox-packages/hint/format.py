def format_u_hint(hint_text):
	return "<font color='grey'>Hint: {0}</font>".format(hint_text)

def format_c_hint(hint_text, hint_id, hint_answer, i):
	if i >= len(hint_id):
		return ""
	hint_answer_id = hint_id[i] + "answer"
	hint = "<div style='padding:10px 10px 10px 0px;'>"
	hint += "<button onclick='show_hint_in_problem({0})'>Show hint</button>".format(i)
	hint += "<p id='{0}' style='display:none'> {1} </p>".format(hint_id[i], hint_text)
	hint += "<p id='{0}' style='display:none'> {1} </p>".format(hint_answer_id, hint_answer)
	hint += "</div>"
	return hint