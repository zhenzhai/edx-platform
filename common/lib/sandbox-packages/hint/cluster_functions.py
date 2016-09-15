import sys
sys.path.append("/Users/janetzhai/Desktop/open_edx/103_edX/devstack/edx-platform/common/lib/sandbox-packages")
from expr_parser import webwork_parser
from expr_parser import Eval_parsed
from collections import deque
from collections import defaultdict

def flatten(tree,tag):
    """flatten a tree
    tag 'c' if it's answer
    tag 't' if it's attempt
    return a flatten sorted list"""
    List=[]
    Queue=deque([tree])
    try:
        while Queue:
            current=Queue.popleft()
            if type(current)==list: 
                if isinstance(current[0],basestring):
                    List.append([current[1],tag,current])
                elif isinstance(current[0][0],basestring) and isinstance(current[0][1],(int, long, float, complex)) and type(current[0][2])==list:
                    List.append([current[0][1],tag,current])
                    Queue.extend(current[1:])
                else:
                    return []
            else:
                return []
    except Exception as error:
        print 'error: current=', str(current)
        return []
    List=sorted(List,key=lambda x: x[0])
    return List


def find_Hits(List,tol = 1+1e-6):
    """ Given a combined list of subtrees from both attempt and answer,
    sorted by value, find the matching pairs of trees
    tol is the tolerance used to define which pairs of values match. 
    Needed because different expressions get different roundoff error
    """
    Hits=[]
    for i in xrange(0,len(List)-1):
        item1 = List[i]
        item2 = List[i+1]
        if item2[0] != 0:
            ratio=item1[0]/item2[0]
        else:
            if item1[0] == 0:
                ratio = 1
            else:
                ratio = 0
        # get the tree node
        node1 = get_top_node(item1)
        node2 = get_top_node(item2)
        if item1[1]!=item2[1] and ratio < tol and ratio > (1/tol) and node1 == node2:
            if item1[1]=='c':
                Hits.append((item1,item2))
            elif item2[1]=='c':
                Hits.append((item2,item1))
            else:
                print "Error in find_Hits. Neither item labeled c"
    return Hits



def find_dominating_hits(Hits,answer,attempt):
    """eliminate dominated hits from input Hits"""
    for i in range(len(Hits)):
        for j in range(len(Hits)):
            if i==j:
                continue
            span1=get_span(Hits[i][0])
            span2=get_span(Hits[j][0])
            # If it is dominated by other hits, marked as 'dc'
            if span1[0]<=span2[0] and span1[1]>=span2[1]:
                Hits[j][0][1]='dc'
    
    final_matches=[]
    for hit in Hits:
        # Do not include hits marked as 'dc'
        if hit[0][1]=='c':
            value=hit[0][0]
            span_c=get_span(hit[0])
            span_a=get_span(hit[1])
            answer_part=answer[span_c[0]:span_c[1]+1]
            attempt_part = attempt[span_a[0]:span_a[1]+1]
            if hit[0][2][0]=='X':
                node=hit[0][2][3]
            else:
                node=hit[0][2][0][3]
            final_matches.append((node,value,answer_part,attempt_part))
    return final_matches



def find_matches(params):
    """ return a list of hits """
    attempt=params['attempt']
    attempt_tree=params['att_tree']
    attempt_list=flatten(attempt_tree,'t')
    
    answer=params['answer']
    answer_tree=params['ans_tree']
    answer_list=flatten(answer_tree,'c')

    # sort by value
    combined_list=sorted(answer_list+attempt_list,key=lambda x: (x[0],len(x[2])))

    # find all hits
    Hits=find_Hits(combined_list)

    # eliminate dominating hits
    final_matches=find_dominating_hits(Hits,answer,attempt)
    
    return final_matches



def get_span(tree):
    """return the starting index and ending index
        used to determine dominating hits"""
    if tree[2][0]=='X':
        return tree[2][2]
    elif type(tree[2][0])==list:
        return tree[2][0][2]
    else:
        print 'Error in get_span'
        return None


def get_top_node(tree):
    """return the starting index and ending index
        used to determine dominating hits"""
    if tree[2][0]=='X':
        return tree[2][3]
    elif type(tree[2][0])==list:
        return tree[2][0][3]
    else:
        print 'Error in get_top_node'
        return None



######## Make a list of dictionaries ##########
def make_params(ans_str, att_str, variable_list={}):
    """
    input: answer string, attemp string,
    optional input: variable dictionary {'variable_name':value to test, 'variable_name2':value}
    return: list of dict with format
        'user_id':d['user_id'],'answer':d['answer'], 'attempt':d['attempt'],
        'ans_tree':eval_tree,'att_tree':eval_tree_att
    """

    parse_tree = webwork_parser.parse_webwork(ans_str)
    if parse_tree[0] == None:
        print 'parse_tree empty'
        return {}
    eval_tree = Eval_parsed.eval_parsed(parse_tree[0], variable_list)
    if eval_tree == None:
        print 'eval_tree empty'
        return {}

    parse_tree_att = webwork_parser.parse_webwork(att_str)
    if parse_tree_att[0] == None:
        print 'parse_tree empty'
        return {}
    eval_tree_att = Eval_parsed.eval_parsed(parse_tree_att[0], variable_list)
    if eval_tree_att == None:
        print 'eval_tree empty'
        return {}

    params = {'answer':ans_str, 'attempt':att_str, 'ans_tree':eval_tree, 'att_tree':eval_tree_att}

    return params



def get_numerical_answer(eval_tree):
    """Get the final value from and evaluation tree"""
    if type(eval_tree[0])==list:
        return eval_tree[0][1]
    else:
        return eval_tree[1]






def equal_len(variable_list):
    """ Check whether all variables has the same size of values to test """
    size_of_list = len(variable_list[variable_list.keys()[0]])
    for key in variable_list:
        if len(variable_list[key]) != size_of_list:
            return False
    return True

def extract_one_value_to_test(variable_values, index):
    """ Extract one value to test for each of the variable """
    variable_list = {}
    for key in variable_values:
        variable_list[key] = variable_values[key][index]
    return variable_list

def make_params_w_variables(ans_str, att_str, variable_values, index):
    """ make param using test value at the passed in index """
    v_list = extract_one_value_to_test(variable_values, index)
    return make_params(ans_str, att_str, v_list)

def find_matches_w_variables(ans_str, att_str, variable_values, test_all=False):
    """ return a list of hits """
    params = make_params_w_variables(ans_str, att_str, variable_values, 0)
    final_matches = find_matches(params)

    if test_all:
        #first check to make sure equal length
        if len(variable_values>1) and ~equal_len(variable_list):
            print 'need to make sure variables all have same number of values'
            return None

        size_of_value_list = len(variable_values[variable_values.keys()[0]])
        for i in xrange(size_of_value_list):
            params = make_params_w_variables(ans_str, att_str, variable_values, i)
            match = find_matches(params)
            if match != final_matches:
                return None
    return final_matches


def show_matching_group_w_variables(ans_str, att_str, variable_values, test_all=False):
    """ can test all values provided in variable_values
    and return a list of hits """
    matches = find_matches_w_variables(ans_str, att_str, variable_values, test_all)
    parse_tree_att = webwork_parser.parse_webwork(att_str)
    matching_exps = []
    if parse_tree_att[0] == None:
        print 'parse_tree empty'
        return None
    if matches:
        for m in matches:
            tree_index = [int(i)+1 for i in m[0].split('.')[1:]]
            node = parse_tree_att[0]
            for t in tree_index:
                node = node[t]
            matching_exps.append(att_str[node[0][1][0]:node[0][1][1]+1])
        return matching_exps
    else:
        return None










