import sqlite3
from random import randint

class Database:
    def __init__(self, db_file = 'warships.db'):
        self.connect(db_file)

    def __del__(self):
        self.db_connect.commit()
        self.cursor.close()
        self.db_connect.close()

    def connect(self, db_file):
        self.db_connect = sqlite3.connect(db_file)
        self.cursor = self.db_connect.cursor()

    def drop_tables(self):
        for table in ['Ships', 'Weapons', 'Hulls', 'Engines']:
            self.cursor.execute('DROP TABLE IF EXISTS {};'.format(table))

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE Ships(
                ship    TEXT PRIMARY KEY,
                weapon  TEXT,
                hull    TEXT,
                engine  TEXT
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE Weapons(
                weapon          TEXT PRIMARY KEY,
                reload_speed    INT,
                rotation_speed  INT,
                diameter        INT,
                power_volley    INT,
                count           INT
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE Hulls(
                hull        TEXT PRIMARY KEY,
                armor       INT,
                type        INT,
                capacity    INT
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE Engines(
                engine  TEXT PRIMARY KEY,
                power   INT,
                type    INT
            );
        ''')
        self.db_connect.commit()

    def insert(self, table, vars):
        query = 'INSERT INTO {} VALUES(' + '?, ' * (len(vars) - 1) + '?);'
        self.cursor.execute(query.format(table), vars)

    def update(self, table, column, new_value, primary_key):
        self.cursor.execute('''
            UPDATE {0}
            SET {1} = {2}
            WHERE {3} = {4};
        '''.format(table, column, new_value, table.lower()[:-1], '"' + primary_key + '"'))

    def select(self, table, primary_key):
        self.cursor.execute('''
            SELECT * FROM {0}
            WHERE {1} = (SELECT {1} FROM Ships
                            WHERE ship = {2});
        '''.format(table, table.lower()[:-1], '"' + primary_key + '"'))
        return self.cursor.fetchall()

    def random_insert(self):
        for ship in range(200):
            self.insert('Ships', ('Ship-'   + str(ship),
                                  'Weapon-' + str(randint(0, 19)),
                                  'Hull-'   + str(randint(0, 4)),
                                  'Engine-' + str(randint(0, 5))))
        for weapon in range(20):
            self.insert('Weapons', ('Weapon-' + str(weapon),
                                    randint(1, 20),
                                    randint(1, 20),
                                    randint(1, 20),
                                    randint(1, 20),
                                    randint(1, 20)))
        for hull in range(5):
            self.insert('Hulls', ('Hull-' + str(hull),
                                  randint(1, 20),
                                  randint(1, 20),
                                  randint(1, 20)))
        for engine in range(6):
            self.insert('Engines', ('Engine-' + str(engine),
                                    randint(1, 20),
                                    randint(1, 20)))

        self.db_connect.commit()

    def random_update(self):
        ship_components = [['weapon', 19], ['hull', 4], ['engine', 5]]
        for ship in range(200):
            component = ship_components[randint(0, 2)]
            self.update('Ships', component[0],
                        '"' + component[0].capitalize() + '-' + str(randint(0, component[1])) + '"',
                        'Ship-' + str(ship))

        weapon_values = [
            'reload_speed',
            'rotation_speed',
            'diameter',
            'power_volley',
            'count']
        for weapon in range(20):
            value = weapon_values[randint(0,4)]
            self.update('Weapons', value, randint(1, 20), 'Weapon-' + str(weapon))

        hull_values = ['armor', 'type', 'capacity']
        for hull in range(5):
            value = hull_values[randint(0, 2)]
            self.update('Hulls', value, randint(1, 20), 'Hull-' + str(hull))

        engine_values = ['power', 'type']
        for engine in range(6):
            value = engine_values[randint(0, 1)]
            self.update('Engines', value, randint(1, 20), 'Engine-' + str(engine))

        self.db_connect.commit()
