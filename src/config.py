import configparser


class Config:
    merge_tables = []
    relation_tables = []

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../resources/config.ini', 'UTF-8')

        index = 1
        while True:
            try:
                merge_table = "MERGE_TABLE_{0}".format(str(index))
                relation_table = "RELATION_TABLE_{0}".format(str(index))
                self.merge_tables.append(
                    {'table': config[merge_table]['TABLE'], 'primary_key': config[merge_table]['PRIMARY_KEY'],
                     'relation_table': config[merge_table]['RELATION_TABLE']})
                self.relation_tables.append(
                    {'table': config[relation_table]['TABLE'], 'primary_key': config[relation_table]['PRIMARY_KEY'],
                     'foreign_key': config[relation_table]['FOREIGN_KEY']})
                index += 1
            except KeyError:
                break
                pass
