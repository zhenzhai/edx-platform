def get_conditional_hints(hint_text_id, i, params):
    if i >= len(hint_text_id):
        #logger.error("index out of range in get_conditional_hints")
        return "", ""
    id_str = hint_text_id[i]

    # id parsing
    try:
        week_pos, problem_pos, part_pos = \
                id_str.find('week'), id_str.find('problem'), id_str.find('part')
        week_id, problem_id, part_id = \
                id_str[week_pos+4:problem_pos], id_str[problem_pos+7:part_pos], id_str[part_pos+4:]
    except:
        print "input hint_text_id incorrect."
        return "", ""
    
    class_address = "hint.hint_class.Week{0}.Prob{1}_Part{2}.Prob{1}_Part{2}".format(week_id, problem_id, part_id)


    '''Read hint class'''
    #class_address = "hint." + package_name + "." + class_name + "." + class_name
    try:
        ClassName = locate(class_address)
    except:
        print "ERROR: syntax error in HINT CLASS!!"
        return "", ""

        try:
        hint_instance = ClassName()
    except TypeError:
        print "ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!"
        return "", ""

    try:
        hint, hint_ans = hint_instance.check_attempt(params)
    except:
        print "ERROR: syntax error in HINT CLASS!!"
        return

    if hint and hint_ans:
        return hint, hint_ans

    return "", ""

