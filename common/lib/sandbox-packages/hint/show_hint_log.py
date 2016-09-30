# Log the time student click the 'show_hint' button

import os
import sys
import MySQLdb
from flask import request, Flask
from flask_cors import CORS, cross_origin


db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

'''Create the table, should be executed only once'''
create_phtb_table_sql = """CREATE TABLE show_hint_click(
                                        id int NOT NULL AUTO_INCREMENT,
                                        problem_name CHAR(255),
                                        problem_part CHAR(255), 
                                        student_username CHAR(255),
                                        time_clicked TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                                        PRIMARY KEY (ID) )"""

#db_cursor.execute(create_phtb_table_sql)                                        


app = Flask(__name__)
CORS(app)

@app.route('/show_hint_button_clicked', methods=['POST'])
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
        insert_sql = """INSERT INTO show_hint_click (problem_name, problem_part, student_username)
                        VALUES(%s,%s, %s)"""  
        db_cursor.execute(insert_sql,new_record)  
        db.commit()
    except:
        db.rollback()
        print "Database has been rolled back because of an Exception !!!"
        print(traceback.format_exc())  

    db.close()
    
  
