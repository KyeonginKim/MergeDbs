import argparse
import sys


def diff(rule_list1, rule_list2):
    set_rule1 = set(rule_list1)
    set_rule2 = set(rule_list2)

    if set_rule1 > set_rule2:
        return list(set_rule1 - set_rule2)
    else:
        return list(set_rule2 - set_rule1)


def arg_parser():
    argp = argparse.ArgumentParser()
    argp.add_argument('-d1', dest='db_path1', required=True)
    argp.add_argument('-d2', dest='db_path2', required=True)

    options = argp.parse_args(sys.argv[1:])
    return options.db_path1, options.db_path2
