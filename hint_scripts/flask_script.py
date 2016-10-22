import os
import sys
import MySQLdb
from flask import request, Flask
from flask_cors import CORS, cross_origin
import traceback
import json

import logging.handlers
import logging
# logging settings
formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s')

log_path = '/home/zzhai/hint_log/show_hint.log'
logger = logging.getLogger('show_hint')
handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 16)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

log_path2 = '/home/zzhai/hint_log/select_student.log'
logger2 = logging.getLogger('select_student')
handler2 = logging.handlers.RotatingFileHandler(log_path2, maxBytes = 262144, backupCount = 16)
handler2.setFormatter(formatter)
logger2.addHandler(handler2)
logger2.setLevel(logging.INFO)


db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

'''Create the table, should be executed only once'''
create_show_hint_click_table_sql = """CREATE TABLE show_hint_click(
                                        id int NOT NULL AUTO_INCREMENT,
                                        problem_name CHAR(255),
                                        problem_part CHAR(255), 
                                        student_username CHAR(255),
                                        time_clicked TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                                        PRIMARY KEY (ID) )"""

#db_cursor.execute(create_show_hint_click_table_sql)  

'''Create the table, should be executed only once'''
create_hint_log_table_sql = """CREATE TABLE hint_log(
                                        id int NOT NULL AUTO_INCREMENT,
                                        problem_name CHAR(255),
                                        problem_part CHAR(255), 
                                        student_username CHAR(255),
                                        hint_content CHAR(255),
                                        attempt CHAR(255),
                                        time_clicked TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                        PRIMARY KEY (ID) )"""                   

#db_cursor.execute(create_hint_log_table_sql)

app = Flask(__name__)
CORS(app)

@app.route('/show_hint_button_clicked', methods=['POST'])
def hint_button():
    logger.info("captured post")
    student_username = request.form["student_name"]
    problem_info = request.form["problem_info"]
    hint_content = request.form["hint"]
    attempt = request.form['attempt']
    logger.info("grabbed input:")
    logger.info("\t student_name {0}, problem_info {1}, hint_content {2}, attempt {3}.".format(student_username, problem_info, hint_content, attempt))
    try:
        week_pos, problem_pos, part_pos = \
             problem_info.find('week'), problem_info.find('problem'), problem_info.find('part')
        week_id, problem_id, part_id = \
                 problem_info[week_pos+4:problem_pos], problem_info[problem_pos+7:part_pos], problem_info[part_pos+4:]
        problem_name = "Week{0}_Problem{1}".format(week_id, problem_id)
        problem_part = part_id
        new_record = (problem_name, problem_part, student_username, hint_content, attempt)
        logger.info("record captured")
    except:
        logger.error("problem_info format wrong: {0}".format(problem_info))
        return "problem_info format wrong: {0}".format(problem_info) 
    
    try:
        insert_sql = """INSERT INTO hint_log (problem_name, problem_part, student_username, hint_content, attempt)
                        VALUES(%s,%s,%s,%s,%s)"""  
        db_cursor.execute(insert_sql, new_record)
        db.commit()
        logger.info("hint logged to db")
    except:
        db.rollback()
        logger.error("Exception {0}".format(traceback.format_exc()))
        return "Database has been rolled back because of an Exception !!!{0}".format(traceback.format_exc())  
    # db.close()
    
    logger.info("return success")
    return 'success'


@app.route('/debug')
def debug():
    return "It is working!"


@app.route('/hint_permission', methods=['POST'])
def select_student():
    logger2.info("captured post")
    username = request.form["username"]
    problem_info = request.form["problem_info"]
    timer_diff = request.form["timer_diff"]
    hint_number = request.form["hint_number"]

    try:
        week_pos, problem_pos, part_pos = \
             problem_info.find('week'), problem_info.find('problem'), problem_info.find('part')
        week_id, problem_id, part_id = \
                 problem_info[week_pos+4:problem_pos], problem_info[problem_pos+7:part_pos], problem_info[part_pos+4:]
        int(week_id)
	week_number = "WEEK{0}".format(week_id)
        logger2.info("record captured {0}".format(week_number))
    except:
        logger2.error("problem_info format wrong: {0}. Return False".format(problem_info))
        return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})

    logger2.info("grabbed username:{0}".format(username))
    select_params = (username,)
    select_sql = """SELECT * FROM hint_assignment
                    WHERE username = %s"""

    try:
        db_cursor.execute(select_sql,select_params)  
        records = list(db_cursor.fetchall())
        logger2.info("fetched list from database")
        if(len(records) == 1):
            student = records[0]
            logger2.info("fetched student log permission of username:{0}.".format(username))
            logger2.info(student)
	    if student[int(week_id)] == '1':
                return json.dumps({'status':'True','timer_diff':timer_diff, 'hint_number':hint_number})
            else:
                return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})
        elif(len(records) == 0):
            logger2.info('No student is fetched with username: {0}. Return False'.format(username))
            return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})
        else:
            logger2.info("Multiple students with the same username {0}. Return False".format(username))
            return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})

    except:
        db.rollback()
        logger2.error("Database has been rolled back because of an Exception below:")
        logger2.error(traceback.format_exc())
        logger2.error("Return False")
        return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})
    
    logger2.error("Return False because of an error.")
    return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})

if __name__ == '__main__':
	app.run(host='0.0.0.0')
