import configparser


class Config:
    """
    destination_tables --> list
    relation_tables --> dict; key(relation_table):string
    """
    destination_tables = []
    relation_tables = {}
    config = configparser.ConfigParser()
    config.read('../resources/config.ini', 'UTF-8')

    def set_destination_tables(self, index):
        config_key = "DESTINATION_TABLE.{0}".format(str(index))
        self.destination_tables.append(
            {'table': self.config[config_key]['TABLE'], 'primary_key': self.config[config_key]['PRIMARY_KEY'],
             'relation_table': self.config[config_key]['RELATION_TABLE']})

    def set_relation_tables(self, relation_table):
        """재귀 함수"""
        config_key = "RELATION_TABLE.{0}".format(relation_table)
        sub_relation_table = self.config[config_key]['RELATION_TABLE']
        self.relation_tables[relation_table] = {
            'table': self.config[config_key]['TABLE'], 'primary_key': self.config[config_key]['PRIMARY_KEY'],
            'foreign_key':self.config[config_key]['FOREIGN_KEY'], 'relation_table': sub_relation_table}

        if sub_relation_table == 'NULL':
            return
        else:
            self.set_relation_tables(sub_relation_table)

    def __init__(self):
        index = 0
        while True:
            try:
                self.set_destination_tables(index)
                try:
                    self.set_relation_tables(self.destination_tables[index]['relation_table'])
                except KeyError:
                    pass
                index += 1
            except KeyError:
                break
                pass
