from src.config import *
from src.util import *
from src.db_util import *
from src.connection import Connection
import sys

db_path_1 = ''
db_path_2 = ''


def print_diff_content(conf_list, content):
    for conf in conf_list:
        table = conf['table']
        pk = conf['primary_key']
        if pk != 'NULL':
            print('========[ {0} {1} Table Diff ]========'.format(table, content))
            print(diff(select_pk_from_table(db_path_1, table, pk), select_pk_from_table(db_path_2, table, pk)))


def print_diff(target_dbs, relation_dbs):
    print_diff_content(target_dbs, "Target")
    print_diff_content(relation_dbs, "Relation")


def merge(target_dbs, relation_dbs):
    connection = Connection(db_path_1)
    connection.attach_database(db_path_2)

    for conf in target_dbs:
        connection.merge_table(conf['table'])

    for conf in relation_dbs:
        connection.merge_table(conf['table'])

    connection.detach_database()


if __name__ == "__main__":
    try:
        config = Config()
        db_path_1, db_path_2 = arg_parser()
        print_diff(config.merge_tables, config.relation_tables)
        merge(config.merge_tables, config.relation_tables)
    except:
        # ===============
        # Error handle
        # ===============
        print("Runtime Error :")
        print("Error Type : ", sys.exc_info()[0])
        print("Unexpected error : ", sys.exc_traceback)
        raise
