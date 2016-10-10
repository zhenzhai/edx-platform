# Script to update the pickle file
# Run this script with the folder that contains all the hint class files,
# it will check for any new hint classes, and add them to MYSQL
# 
# NOTICE: Name of the hint class has to be the same as the hint class file
#
# Name: Xueyang Li
# Date: Sep 21, 2016

from pydoc import locate
import os
from os import listdir
from os.path import isfile, join
import sys
import MySQLdb

# Folder path on developer's macbook pro
# ~/Desktop/cse/edex/Developers_repo/hint_database/testHintClassFolder

db = MySQLdb.connect("localhost","root","","ucsd_cse103" )
db_cursor = db.cursor()

'''Create the table, should be executed only once'''
create_phtb_table_sql = """CREATE TABLE problem_to_hint(
                                        ID int NOT NULL AUTO_INCREMENT,
                                        PROBLEM_NAME CHAR(255), 
                                        HINT_CLASSES CHAR(255), 
                                        PRIMARY KEY (ID) )"""

#db_cursor.execute(create_phtb_table_sql)                                        

#hint_class_dir = 'testHintClassFolder'

if __name__ == "__main__":
    
    root = "hint_class/"
    folder_path = raw_input("Type in Week ID:\n")
    folder_path = root + folder_path

    hint_class_files = []
    for f in listdir(os.path.expanduser(folder_path)):
        if isfile(join(os.path.expanduser(folder_path), f)) and \
                f.endswith('.py') and f != '__init__.py' and f != 'template.py':
            hint_class_files.append(f)

    hint_classes = []
    for n in hint_class_files:
        hint_classes.append(os.path.splitext(n)[0]) 

    class_path = folder_path#[folder_path.find(hint_class_dir):]

    '''Fetch all the records from database'''
    db_cursor.execute("SELECT * FROM problem_to_hint")
    records = list(db_cursor.fetchall())
    # print records

    for class_name in hint_classes:
        class_address = class_path.replace('/','.') + "." + class_name + "." + class_name
        print class_address
        ClassName = locate(class_address)

        try:
            hint_instance = ClassName()
        except TypeError:
            sys.exit("ERROR: name of the file: " + class_name + " has to be the same as its class name!")
        
        problem_list = hint_instance.get_problems()

        ''' Add new prblem-hint pair to the dictionary '''
        for problem_name in problem_list:
            
            '''Check whether the problem is already in the database or not''' 
            isInDB = False             
            for record in records[:]:
                
                if(problem_name == record[1]):
                    isInDB = True
                    hint_class_string = record[2]
                    if class_name not in hint_class_string:
                        hint_class_string += "," + class_address
                        
                        '''Update the selected problem with the new hint class string'''
                        try:
                            update_sql = """UPDATE problem_to_hint 
                                            SET HINT_CLASSES = %s
                                            WHERE PROBLEM_NAME = %s"""
                            db_cursor.execute(update_sql,(hint_class_string,problem_name))
                            db.commit()
                        except:
                            db.rollback()
                            print "Database has been rolled back because of an Exception !!!"
                            print(traceback.format_exc())                              

                        '''Need to update the records(tuple of tuples) too'''
                        new_record = (record[0], record[1], hint_class_string)
                        records.remove(record)
                        records.append(new_record)

                    break

            '''If the problem is not in the database, add a new record to DB'''
            if(not isInDB):

                new_record = (problem_name,class_address)
                
                try:
                    insert_sql = """INSERT INTO problem_to_hint (PROBLEM_NAME, HINT_CLASSES)
                                    VALUES(%s,%s)"""  
                    db_cursor.execute(insert_sql,new_record)  
                    db.commit()
                except:
                    db.rollback()
                    print "Database has been rolled back because of an Exception !!!"
                    print(traceback.format_exc())  

                '''Need to append the new_record to the records(tuple of tuples) too'''
                new_record_with_id = (len(records) + 1, problem_name, class_address)
                records.append(new_record_with_id)
    db.close()

  
