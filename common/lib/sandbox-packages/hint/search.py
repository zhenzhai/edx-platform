# Script to search for the right hint
# Given problem ID, search in hint_dict, find related hint_classes, then output the hint if certain condition is satisfied
# Name: Zhipeng Yan
# Date: Sep 21, 2016

__author__ = 'zpyan'

import MySQLdb, json, types
from pydoc import locate



def search(id_str_list, i, p):
    #id_str is like: cse103fall2016week1problem1part1
    if i < len(id_str_list):
        id_str = id_str_list[i]
    else:
        return ""

    # constants
    mapping_file = 'problems_mapping.tsv'
    mapping_table = 'ucsd_cse103.pos_to_problem'
    hint_table = 'ucsd_cse103.problem_to_hint'
    hint_class_folder = 'hint_class.'

    # connect to db
    try:
        db = MySQLdb.connect("localhost", "root", "", "ucsd_cse103")
        db_cursor = db.cursor()
    except Exception:
        # logger.error('Failed to connect to db.')
        return "" 

    ''' THIS INIT SHOULD BE EXECUTED ONLY AT THE BEGINNING '''
    init = """
            DROP TABLE IF EXISTS {table_name};
            CREATE TABLE {table_name}(
                id int NOT NULL AUTO_INCREMENT,
                week_id char(255),
                problem_id char(255),
                problem_name char(255),
                PRIMARY KEY (id)
                );
            LOAD DATA LOCAL INFILE '{file_name}' INTO TABLE {table_name}
            FIELDS TERMINATED BY '\t'
            ENCLOSED BY "'"
            LINES TERMINATED BY '\n'
            (week_id, problem_id, problem_name);
            """
    # You need to open mysql with --local-infile mode to import local file.
    # db_cursor.execute(init.format(table_name = mapping_table, file_name = mapping_file))



    # id parsing
    try:
        week_pos, problem_pos, part_pos = \
                id_str.find('week'), id_str.find('problem'), id_str.find('part')
        week_id, problem_id, part_id = \
                id_str[week_pos+4:problem_pos], id_str[problem_pos+7:part_pos], id_str[part_pos+4:]
    except:
        print "input id_str incorrect."
        return ""

    if not (week_id.isdigit() and problem_id.isdigit() and part_id.isdigit()):
        print 'week/problem id not found.'
        return ""

    query = """
            SELECT problem_name
            FROM {}
            WHERE week_id = '{}' and problem_id = '{}';
            """
    db_cursor.execute(query.format(mapping_table, week_id, problem_id))
    result = db_cursor.fetchall()

    if result == ():
        # logger.error('week {} problem {} has not yet been added.'.format(week_id, problem_id))
        return ""
    else:
        problem_name = result[0][0]

    query = """
            SELECT hint_classes
            FROM {}
            WHERE problem_name = '{}';
            """
    db_cursor.execute(query.format(hint_table, problem_name + '/part' + part_id))
    result = db_cursor.fetchall()

    if result == ():
        print problem_name + " has not been added yet."
        return ""
    else:
        candidate_hint_list = result[0][0].split(',')

    # searching for appropriate hint
    for i in xrange(len(candidate_hint_list)):
        candidate_hint_class = locate(candidate_hint_list[i])
        if candidate_hint_class is None:
            print 'Hint class [{}] not found. Could be file missing or class name not consistent with the file name.'.format(candidate_hint_list[i])
            continue

        if type(candidate_hint_class) != types.ClassType:
            print candidate_hint_list[i] + ' is not a class.'
            continue

        candidate_hint = candidate_hint_class()
        hint_content, hint_answer = candidate_hint.check_attempt(p)
        if hint_content and hint_answer:
            print 'hint found'
            return hint_content, hint_answer

    print 'No appropriate hint found'
    return ""
