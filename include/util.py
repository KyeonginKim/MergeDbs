import sqlite3
import argparse
import sys


def diff(rule_list1, rule_list2):
    set_rule1 = set(rule_list1)
    set_rule2 = set(rule_list2)

    if set_rule1 > set_rule2:
        return list(set_rule1 - set_rule2)
    else:
        return list(set_rule2 - set_rule1)


def arg_parser():`
    argp = argparse.ArgumentParser()
    argp.add_argument('-d1', dest='db_path1', required=True)
    argp.add_argument('-d2', dest='db_path2', required=True)
    argp.add_argument('-r', dest='rule_set_name', required=True)

    options = argp.parse_args(sys.argv[1:])
    return options.db_path1, options.db_path2, options.rule_set_name


def get_data(url, name):
    connection = sqlite3.connect(url)
    if connection is None:
        print("sqlite connection fail : [ url : {0} ]".format(url))
        return []
    cursor = connection.cursor()
    query = "SELECT name FROM Rule WHERE ruleSet = \"{0}\";".format(name)
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    db_path1, db_path2, rule_set_name = arg_parser()
    print(arg_parser())
    print(diff(get_data(db_path1, rule_set_name), get_data(db_path2, rule_set_name)))