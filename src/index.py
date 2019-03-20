# from person import *
from database import *

# Database info
database_path = "database.db" # Path to database file

# Testing the Person class
database = Database(database_path)

database.run('CREATE TABLE people (ID varchar(100), FirstName varchar(100), LastName varchar(100)), PhysicalFeatures varchar(100), RegisteredTime varchar(100), HashFinger varchar(100)')
