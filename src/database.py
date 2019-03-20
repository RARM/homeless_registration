import sqlite3

# Treating the database as a class
class Database():
    def __init__(self, path): # When you create a Database object, the argument is the path to the database
        self.connection = sqlite3.connect(path)
        self.c = self.connection.cursor()

    def check(self):
        self.c.execute('SELECT name FROM sqlite_master WHERE type="table"')
        tables = self.c.fetchall()

        if tables == []:# Checking if there are tables, returns true if there is at lest one table
            # Visit https://www.sqlite.org for documentation on sqlite3 commands
            # cursor.execute("CREATE TABLE test (ID int, Name varchar(100))") # Creating tables
            print("The database doesn't have any tables.")
            return False
        else:
            print("The database is connected and there is one or more tables availables.")
            return True

    def run(self, command): # Equivalent to the execute() method
        info = self.c.execute(command)
        return info

    def getTables(self): # Get tables returns a list of the tables names as strings
        self.c.execute('SELECT name FROM sqlite_master WHERE type="table"')
        tables = self.c.fetchall()
        tables_list = list()
        for i in range(len(tables)):
            tables_list.append(tables[i][0])
        return tables_list

# Test
# myDatabase = Database("example.db")
# print(myDatabase.check())
# print(myDatabase.getTables())
