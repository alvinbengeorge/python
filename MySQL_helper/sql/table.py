from .database import DATABASE
from .Structs import Table, safe_get, dsb_str

class TABLE:
    def __init__(self, Database: DATABASE, name = None):
        self.DATABASE = Database
        self.cursor = self.DATABASE.cursor
        self.cursor.execute("show tables;")
        self.tables = [i[0] for i in self.cursor.fetchall()]
        self.NAME = name
        if not name:
            self.NAME = safe_get(self.tables, 0)

    
    def describe(self, name: str):
        self.cursor.execute("describe {}".format(name))
        return self.cursor.fetchall()

    
    def view_table(self, name: str):
        self.cursor.execute(f"select * from {name}")
        return Table(self.cursor.fetchall(), dsb_str(self.describe(name)))

    
    def delete(self):
        if self.NAME:
            self.cursor.execute("Drop table {};".format(self.NAME))

class Change:
    def __init__(self, table: TABLE):
        self.TABLE = table

    def set(self, _conditions: str = "",**kwargs):
        print(kwargs)
        x = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
        query = f"update {self.TABLE.NAME} set {x} {f'where {_conditions}' if _conditions else ''};"
        print(query)
        self.TABLE.cursor.execute(query)
        if self.TABLE.DATABASE.AUTOSAVE:
            self.TABLE.DATABASE.DB.commit()