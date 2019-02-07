from src.connection import Merge


def execute(url, query):
    connection = Merge(url)
    result = connection.execute_query(query)
    connection.close()
    return result


def select_pk_from_table(url, table, pk):
    query = "SELECT {0} FROM {1};".format(pk, table)
    return execute(url, query)


def select_pk_from_table_by(url, table, pk, fk_column, fk_value):
    query = "SELECT {0} FROM {1} WHERE {2} = \"{3}\";".format(pk, table, fk_column, fk_value)
    return execute(url, query)


def insert_relation_data(url, table, pk, fk_column, fk_value):
    """ON DUPLICATE KEY UPDATE b = b + c;"""
    sub_query = "SELECT {0} FROM {1} WHERE {2} = {3};".format(pk, table, fk_column, fk_value)
    query = "INSERT INTO {0} {1} ON DUPLICATE KEY UPDATE()".format(table, sub_query)

    return execute(url, query)
