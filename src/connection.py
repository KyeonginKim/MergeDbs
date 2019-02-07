import sqlite3

var = 'toMerge'


class Merge:
    def __init__(self, url):
        self.connection = connection = sqlite3.connect(url)
        if connection is None:
            print("Database Connection Fail : [ URL : {0} ]".format(url))
            self.close()

    def close(self):
        self.connection.close()

    def transaction_begin(self):
        query = 'BEGIN;'
        self.execute_query(query)

    def transaction_commit(self):
        query = 'COMMIT;'
        self.execute_query(query)

    def attach_database(self, contacts):
        query = 'ATTACH \'{0}\' AS {1};'.format(contacts, var)
        self.execute_query(query)

    def detach_database(self):
        query = 'DETACH {0};'.format(var)
        self.execute_query(query)

    def merge_table(self, table, pk):
        query = "INSERT INTO {0} SELECT * FROM {1} WHERE {2} NOT IN (SELECT DISTINCT {2} FROM MAIN.{0});"\
            .format(table, var + '.' + table, pk)
        self.execute_query(query)

    def merge_relation_table(self, table, pk, fk_column, fk_value):
        """ON DUPLICATE KEY UPDATE b = b + c;"""
        sub_query = "SELECT {0} FROM {1} WHERE {2} == {3}".format(pk, table, fk_column, fk_value)
        query = "INSERT INTO {0} {1} ON DUPLICATE KEY UPDATE({2}=MAX({2})+1)".format(table, sub_query, pk)

        self.execute_query(query)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception:
            print("Query with Error : ", query)
            raise
        finally:
            cursor.close()

        return result
