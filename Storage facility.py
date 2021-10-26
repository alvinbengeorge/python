import pickle
import csv
import os

class Table:
    def __init__(self, filename):
        self.filename = filename+".csv"
        with open(self.filename, mode = "r") as file:
            self.reader = list(csv.reader(file))
        self.length = len(list(self.reader[0])) if len(list(self.reader))>0 else 0
        
    def create_table(self, **headers):
        self.reader.clear()
        self.reader.append(list(headers.keys()))
        self.length = len(headers)
        return True

    def table_exists(self):
        return True if len(self.reader)>0 else False

    def reset_length(self):
        self.length = len(self.reader[0]) if len(self.reader)>0 else 0

    def add_values(self, *values):
        values = list(values)
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
        with open(self.filename,mode = "w") as file:
            writer = csv.writer(file)
            writer.writerows(self.reader)
        print(self.reader)
        return True

    def show_data(self, mode = "string"):
        if mode == "string": [print(i) for i in self.reader]
        else: return self.reader

    def describe(self):
        return self.reader[0] if self.table_exists() else []

class Variables:
    def __init__(self, filename):        
        self.filename = filename+".dat"
        self.data = {}
        if self.filename in os.listdir():
            with open(self.filename, mode = 'rb') as file:
                self.data = pickle.load(file)
        else:
            with open(self.filename, mode = 'wb') as file:
                pickle.dump(self.data, file)

    def edit(self, variable_name, value):
        self.data[variable_name] = value
        return True

    def pass_all(self, **variables):
        self.data = variables
        return True

    def save(self):
        with open(self.filename, mode = 'wb') as file:
            pickle.dump(self.data, file)
            return True

    def show_data(self):
        return self.data

