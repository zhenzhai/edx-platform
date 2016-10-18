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
log_path = '/home/zzhai/hint_log/select_student.log'
logger = logging.getLogger('select_student')
handler = logging.handlers.RotatingFileHandler(log_path, maxBytes = 262144, backupCount = 16)
formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor() 

app = Flask(__name__)
CORS(app)

@app.route('/hint_permission', methods=['GET'])
def index():
    logger.info("captured post")
    username = request.form["username"]
    problem_info = request.form["problem_info"]
    timer_diff = request.form["timer_diff"]
    hint_number = request.form["hint_number"]

    try:
        week_pos, problem_pos, part_pos = \
             problem_info.find('week'), problem_info.find('problem'), problem_info.find('part')
        week_id, problem_id, part_id = \
                 problem_info[week_pos+4:problem_pos], problem_info[problem_pos+7:part_pos], problem_info[part_pos+4:]
        week_number = "WEEK{0}".format(week_id)
        logger.info("record captured {0}".format(week_number))
    except:
        logger.error("problem_info format wrong: {0}. Return False".format(problem_info))
        return json.dumps({'status':'False','timer_diff':timer_diff, 'hint_number':hint_number})

    logger.info("grabbed username:{0}".format(username))
    select_params = (username)
    select_sql = """SELECT * FROM hint_assignment
                    WHERE username = %s"""

    try:
        db_cursor.execute(select_sql,select_params)  
        records = list(db_cursor.fetchall())
        logger.info("fetched list from database")
        if(len(records) == 1):
            student = records[0]
            logger.info("fetched student log permission of username:{0}.".format(username))
            if student[week_number] == '1':
                return json.dumps({'status':'True','timer_diff':timer_diff})
            else:
                return json.dumps({'status':'False','timer_diff':timer_diff})
        elif(len(records) == 0):
            logger.info('No student is fetched with username: {0}. Return False'.format(username))
            return json.dumps({'status':'False','timer_diff':timer_diff})
        else:
            logger.info("Multiple students with the same username {0}. Return False".format(username))
            return json.dumps({'status':'False','timer_diff':timer_diff})

    except:
        db.rollback()
        logger.error("Database has been rolled back because of an Exception below:")
        logger.error(traceback.format_exc())
        logger.error("Return False")
        return json.dumps({'status':'False','timer_diff':timer_diff})
    
    logger.error("Return False because of an error.")
    return json.dumps({'status':'False','timer_diff':timer_diff})

app.run(host='0.0.0.0')
