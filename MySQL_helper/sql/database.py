import mysql.connector as m

class DATABASE:
    def __init__(self, username: str, password: str, database: str=None, autosave: bool=False, host="localhost", DB: m.connection_cext.CMySQLConnection = None):
        self.DB = m.connect(
            username=username,
            passwd=password,
            database=database,
            host=host
        ) if not DB else DB
        self.cursor = self.DB.cursor(buffered=True)
        self.AUTOSAVE = autosave

    def show_databases(self, DB: m.connection_cext.CMySQLConnection = None):
        self.cursor.execute("SHOW DATABASES;")
        return [i[0] for i in self.cursor.fetchall()]

    def create_database(self, name: str):
        self.cursor.execute(f"CREATE DATABASE {name}")

    def raw_execute(self, query: str):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def change_database(self, name: str):
        self.cursor.execute("use {}".format(name))

    def commit(self):
        self.DB.commit()