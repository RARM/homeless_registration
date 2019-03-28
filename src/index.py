# from person import *
from database import *

# Database info
database_path = "database.db" # Path to database file

# Testing the Person class
database = Database(database_path)

if not (database.check()):
    database.run('CREATE TABLE people (UserID varchar(9), FirstName varchar(100), LastName varchar(100)), Height varchar(100), EyesColor varchar(100), HairColor varchar(100), Gender varchar(100), Ethnicity varchar(100),  RegisteredTime varchar(100), HashFinger varchar(100), PRIMARY KEY(UserID)' )
