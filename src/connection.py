import sqlite3

var = 'toMerge'


class Connection:
    def __init__(self, url):
        self.connection = connection = sqlite3.connect(url)
        if connection is None:
            print("database connection fail : [ url : {0} ]".format(url))
            self.close()

    def close(self):
        self.connection.close()

    def attach_database(self, contacts):
        query = 'attach \'{0}\' as {1};'.format(contacts, var)
        self.execute_query(query)

    def detach_database(self):
        query = 'detach {0}'.format(var)
        self.execute_query(query)

    def merge_table(self, table):
        query = 'insert into {0} select * from {1};'.format(table, var + '.' + table)
        self.execute_query(query)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            print("query : ", query)
            cursor.execute(query)
            result = cursor.fetchall()
        finally:
            cursor.close()

        return result
