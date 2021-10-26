import pickle
import csv
import os

class Table:
    def __init__(self, filename):
        self.filename = filename+".csv"
        self.open_file = open(self.filename, mode = "r+",newline='')
        self.reader = list(csv.reader(self.open_file))
        self.open_file.close()
        self.open_file = open(self.filename, mode = "w+",newline='')
        self.length = len(list(self.reader[0])) if len(list(self.reader))>0 else 0
        
    def create_table(self, **headers):
        self.reader.clear()
        self.reader.append(list(headers.keys()))
        self.reader.append([str(i) for i in list(headers.values())])
        self.length = len(headers)
        return True

    def table_exists(self):
        return True if len(self.reader)>1 else False

    def reset_length(self):
        self.length = len(self.reader[0]) if len(self.reader)>0 else 0

    def add_values(self, *values):
        if not self.table_exists():
            return False
        elif len(values) == self.length:
            self.reader.append(values)
            return True
        elif len(values) < self.length:
            for i in range(self.length - len(values)):
                values.append(None)
            self.reader.append(values)
            return True
        else:
            self.reader.append(values[:self.length])
            return True

    def commit(self):
        writer = csv.writer(self.open_file)
        writer.writerows(self.reader)
        print(self.reader)
        self.open_file.close()
        self.open_file = open(self.filename, mode = "w+",newline='')
        return True

    def show_data(self):
        return self.reader
        
        
a = Table("try")
a.create_table(b = int, c = str)
for i in range(10):
    print(a.table_exists())
    a.add_values(i,i+1)
print(a.show_data())
print("-"*10)
print(a.commit())
print(a.show_data())
