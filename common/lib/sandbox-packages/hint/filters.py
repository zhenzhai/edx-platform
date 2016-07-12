import cluster_functions
from xml.sax.saxutils import escape

def hint_wrong_sign():
	return "Please double check your answer to make sure your sign is correct."

def hint_fraction():
	return "Please double check your answer to make sure it is an integer."

def hint_numerical():
	return "Please write an expression instead of a number."

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

def escape_html(html_code):
    return escape(html_code.replace('"', "&quot;"))

def redirect_hint(text, unit_id):
    html_code = '<a href="/jump_to_id/{0}" target="_blank">{1}</a>'.format(str(unit_id), text)
    color = "grey"
    html_code = '<font color={0}>{1}</font>'.format(color, html_code)
    return escape_html(html_code)[1:-1]