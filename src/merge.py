from src.config import *
from src.util import *
from src.db_util import *
from src.connection import Merge


destination = ''
source = ''


def get_relation_table_contents(diff_list, relation_table, relation_table_info_dict):
    print('[ {0} Relation Table Diff ]'.format(relation_table))
    for pk in diff_list:
        relation_dict = relation_table_info_dict[relation_table]
        print("---->",select_pk_from_table_by(
            source, relation_dict['table'], relation_dict['primary_key'],  relation_dict['foreign_key'], pk[0]))


def get_diff_content(destination_table_info_list, relation_table_info_dict):
    for conf in destination_table_info_list:
        table = conf['table']
        pk = conf['primary_key']

        diff_list = diff(select_pk_from_table(destination, table, pk), select_pk_from_table(source, table, pk))
        print('[ Source.{0} -  Destination.{0} Table Diff ]'.format(table))
        print("--->", diff_list)

        get_relation_table_contents(diff_list, conf['relation_table'], relation_table_info_dict)


def insert_relation_table_data(destination_table_info_list, relation_table_info_dict):
    print('=================================')
    get_diff_content(destination_table_info_list, relation_table_info_dict)
    print('=================================')


def merge(destination_table_info_list, relation_dict):
    """ Merge Logic
    attach 'source_db_path' as toMerge;
    BEGIN;
    insert into Table select * from toMerge.Table;
    COMMIT;
    detach toMerge;
    """
    connection = Merge(destination)
    # cannot ATTACH database within transaction
    connection.attach_database(source)
    connection.transaction_begin()
    for conf in destination_table_info_list:
        dest_pk = conf['primary_key']
        connection.merge_table(conf['table'], dest_pk)
        relation_dict = relation_dict[conf['relation_table']]
        connection.merge_relation_table(
            relation_dict['table'], relation_dict['primary_key'],  relation_dict['foreign_key'], dest_pk)
    connection.transaction_commit()
    connection.detach_database()


if __name__ == "__main__":
    try:
        config = Config()
        destination, source = arg_parser()
        insert_relation_table_data(config.destination_tables, config.relation_tables)
        merge(config.destination_tables, config.relation_tables)
    except RuntimeError as ex:
        # ===============
        # Error handle
        # ===============
        print("Unexpected error : ", ex.__traceback__)
        raise
