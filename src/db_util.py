from src.connection import Connection


def execute(url, query):
    connection = Connection(url)
    result = connection.execute_query(query)
    connection.close()
    return result


def select_pk_from_table(url, table, pk):
    query = "SELECT {0} FROM {1};".format(pk, table)
    return execute(url, query)
