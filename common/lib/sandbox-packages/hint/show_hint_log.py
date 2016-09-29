# Log the time student click the 'show_hint' button

import os
import sys
import MySQLdb
from flask import request, Flask


db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

'''Create the table, should be executed only once'''
create_phtb_table_sql = """CREATE TABLE SHOW_HINT_CLICK(
                                        ID int NOT NULL AUTO_INCREMENT,
                                        PROBLEM_NAME CHAR(255),
                                        PROBLEM_PART CHAR(255), 
                                        STUDENT_USERNAME CHAR(255),
                                        TIME_CLICKED TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                                        PRIMARY KEY (ID) )"""

db_cursor.execute(create_phtb_table_sql)                                        


app = Flask(__name__)

@app.route('/show_hint_clicked', methods=['POST'])
def index():
    student_username = request.form["student_name"]
    problem_info = request.form["problem_info"]
    week_pos, problem_pos, part_pos = \
            id_str.find('week'), id_str.find('problem'), id_str.find('part')
    week_id, problem_id, part_id = \
            id_str[week_pos+4:problem_pos], id_str[problem_pos+7:part_pos], id_str[part_pos+4:]
    problem_name = "Week{0}_Problem{1}".format(week_id, problem_id)
    problem_part = part_id

    new_record = (problem_name, problem_part, student_username)
    
    try:
        insert_sql = """INSERT INTO SHOW_HINT_CLICK (PROBLEM_NAME, PROBLEM_PART, STUDENT_USERNAME)
                        VALUES(%s,%s, %s)"""  
        db_cursor.execute(insert_sql,new_record)  
        db.commit()
    except:
        db.rollback()
        print "Database has been rolled back because of an Exception !!!"
        print(traceback.format_exc())  

    db.close()

  
