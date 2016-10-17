# Script to generate 120 random hint users for each week
# 
# Name: Xueyang Li
# Date: Oct 01, 2016

import csv
import os
import MySQLdb
import random
import sys
import traceback

db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

# number_of_hint_candidates = 120
number_of_weeks = 7

'''Create the table, should be executed only once'''
create_phtb_table_sql = """CREATE TABLE hint_assignment(
                                        ID INT,
                                        USERNAME CHAR(255), 
                                        NAME CHAR(255), 
                                        EMAIL CHAR(255), 
                                        WEEK4 CHAR(255), 
                                        WEEK5 CHAR(255), 
                                        WEEK6 CHAR(255), 
                                        WEEK7 CHAR(255), 
                                        WEEK8 CHAR(255), 
                                        WEEK9 CHAR(255), 
                                        WEEK10 CHAR(255)
                                         )"""

#db_cursor.execute(create_phtb_table_sql)  

'''Server code to return whether a student is a hint candidate or not'''
def check_hint_candidate(user_id, username, name, email, week_number):
    select_params = (user_id,username,name,email)
    select_sql = """SELECT * FROM hint_assignment
                    WHERE id = %s
                    AND   username = %s
                    AND   name = %s
                    AND   email = %s"""

    try:
        db_cursor.execute(select_sql,select_params)  
        db.commit()
        records = list(db_cursor.fetchall())
        
        if(len(records) == 1):
            student = records[0]

            return (student[week_number] == '1')

        elif(len(records) == 0):
            print 'No student is fetched, something wrong with the input parameters'
        else:
	    return False

    except:
        db.rollback()
        print "Database has been rolled back because of an Exception !!!"
        print(traceback.format_exc())


'''Generate the random hint candidates from given all_students.csv'''
def generate_hint_candidates():
        # file_path = raw_input("Type in relative path of csv file:\n")
    file1_path = "all_students.csv"
    num_of_weeks = 7 

    student_list = []

    print "reading all_students.csv"
    with open(file1_path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            student_list.append( [row[0],row[1],row[2],row[3],0,0,0,0,0,0,0] )
    f.close()

    student_list.pop(0)

    print "assigning 0/1 to students"
    for i in range(num_of_weeks):
        # Before changed: Assign certain number of students 1, other students 0
        # After changed: Assign every student 1 or 0 with 50% possibility    
        
        for student in student_list:
            if(random.random() >= 0.5):
                student[i + 4] = 1

    print "inserting to database"
    for student in student_list:
        student_record = tuple(student)
        insert_sql = """INSERT INTO hint_assignment 
                (ID,USERNAME,NAME,EMAIL,WEEK4,WEEK5,WEEK6,WEEK7,WEEK8,WEEK9,WEEK10)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""  
        
        try:
            db_cursor.execute(insert_sql,student_record)  
            db.commit()
        except:
            db.rollback()
            print "Database has been rolled back because of an Exception !!!"
            print(traceback.format_exc())
    print "done"

if __name__ == "__main__":

    #generate_hint_candidates()

    # TEST
    # if(check_hint_candidate(75,'a-amir01','Amir Assadollahzadeh', 'amirassad1373@gmail.com', 10)):
    #     print 'correct'
    # else:
    #     print 'not correct'
