from os import listdir
from os.path import isfile, join, expanduser, splitext
from pydoc import locate
import traceback
base_dir = "/edx/app/edxapp/edx-platform/common/lib/sandbox-packages/hint/"

def get_first_universal_hints(params):
    'Read first universal hint functions'''
    uni_folder_name = base_dir+'hint_class/first_Universal'
    first_u_hints = []
    for f in listdir(expanduser(uni_folder_name)):
        if isfile(join(expanduser(uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            first_u_hints.append(splitext(f)[0])

    package_name = 'hint.hint_class.first_Universal'
    if len(params['att_tree']) > 1:
        test_str = ""
        for f_name in first_u_hints:
            f_address = package_name + "." + f_name
            try:
                uni_f = locate(f_address)
            except:
                traceback.print_exc()
                print "ERROR: locate of universal hint function {0} failed.".format(f_address)
                return

            try:
                hint = uni_f.check_attempt(params)
            except:
                traceback.print_exc()
                print "ERROR: check_attempt of universal hint function {0} failed.".format(f_address)
                return

            if hint:
                return hint


def get_last_universal_hints(params):
    'Read last universal hint functions'''
    l_uni_folder_name = base_dir+'hint_class/last_Universal'
    last_u_hints = []
    for f in listdir(expanduser(l_uni_folder_name)):
        if isfile(join(expanduser(l_uni_folder_name), f)) and \
                f.endswith('.py') and f != '__init__.py':
            last_u_hints.append(splitext(f)[0])

    # Try last universal hint
    package_name = 'hint.hint_class.last_Universal'
    last_universal_hint = ""
    for f_name in last_u_hints:
        f_address = package_name + "." + f_name
        try:
            uni_f = locate(f_address)
        except:
            print("ERROR: syntax error in universal hint function!!")
            return
        try:
            hint = uni_f.check_attempt(params)
        except:
            print("ERROR: syntax error in universal hint function!!")
            return
        if hint:
            return hint
