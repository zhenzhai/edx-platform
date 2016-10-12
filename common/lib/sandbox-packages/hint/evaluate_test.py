from hint_class_helpers.make_params import make_params
from hint_class_helpers.get_numerical_answer import get_numerical_answer
from hint_class_helpers.find_matches import find_matches
from hint_class_helpers.find_matches_w_variables import find_matches_w_variables
import MySQLdb


# import logging.handlers
# import logging
# # logging settings
# log_path = 'evaluate.log'
# logger = logging.getLogger('evaluate')
# handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 16)
# formatter = logging.Formatter('%(asctime)s - %(name)s: EVAL %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)

db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

'''Create the table, should be executed only once'''
create_eval_table_sql = """CREATE TABLE eval_info(
                                        ID int NOT NULL AUTO_INCREMENT,
                                        attempt CHAR(255), 
                                        answer CHAR(255), 
                                        time_clicked TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                                        PRIMARY KEY (ID) )"""

#db_cursor.execute(create_eval_table_sql)    

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


def evaluate_test(ans, att):
	ans = ans.strip("\[")
	ans = ans.strip("\]")
	ans = ans.replace("{","")
	ans = ans.replace("}","")
	att = att.strip("'")
	try:
		update_sql = """UPDATE eval_info 
					SET attempt = %s
					SET answer = %s"""
		db_cursor.execute(update_sql,(att,ans))
		db.commit()
	except:
		db.rollback()
		print "Database has been rolled back because of an Exception !!!"
		#print(traceback.format_exc())  

	p = make_params(ans, att)
	if p == {}:
		#logger.info("param empty from evaluate")
		return False
	att_value = get_numerical_answer(p['att_tree'])
	ans_value = get_numerical_answer(p['ans_tree'])
	final_pairs = find_matches(p)
	#logger.info("output matching: {0}.".format(final_pairs))

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
