def get_conditional_hints(hint_text_id, i, params):
    if i >= len(hint_id):
        #logger.error("index out of range in get_conditional_hints")
        return ""

    # TODO: search from DB 

    '''Read hint class'''
    folder_name = path
    hint_classes = []
    for f in listdir(os.path.expanduser(folder_name)):
        if isfile(join(os.path.expanduser(folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py' and f != 'template.py':
            hint_classes.append(os.path.splitext(f)[0])

    folder_name = path
    package_name = folder_name.replace('/', '.')
    for class_name in hint_classes:
        class_address = package_name + "." + class_name + "." + class_name
        try:
            ClassName = locate(class_address)
        except:
            print "ERROR: syntax error in HINT CLASS!!"
            return

        try:
            hint_instance = ClassName()
        except TypeError:
            print "ERROR: name of the HINT CLASS has to be the same as the name of the FILE !!"
            return

        try:
            hint, hint_ans = hint_instance.check_attempt(params)
        except:
            print "ERROR: syntax error in HINT CLASS!!"
            return

        if hint:
            return hint, hint_ans

