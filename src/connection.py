import sqlite3

var = 'toMerge'


class Connection:
    def __init__(self, url):
        self.connection = connection = sqlite3.connect(url)
        if connection is None:
            print("Database Connection Fail : [ URL : {0} ]".format(url))
            self.close()

    def close(self):
        self.connection.close()

    def attach_database(self, contacts):
        query = 'ATTACH \'{0}\' AS {1};'.format(contacts, var)
        self.execute_query(query)

    def detach_database(self):
        query = 'DETACH {0};'.format(var)
        self.execute_query(query)

    def merge_table(self, table, pk):
        query = 'INSERT INFO {0} SELECT * FROM {1} WHERE {2} NOT IN (SELECT {2} FROM main.{0});'\
            .format(table, var + '.' + table, pk)
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
