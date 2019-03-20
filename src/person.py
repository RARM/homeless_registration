import datetime
import time

# DOB = datetime.datetime(yyyy, mm, dd)
# Using the Person class. Person(name, datetime.datetime(yyyy, mm, dd), )
class Person:
    def __init__(self, name, DOB, physicalFeatures):
        self.name = name
        self.DOB = DOB
        self.physicalFeatures = physicalFeatures
        self.signInTime = time.time()
        self.age = self.computeAge()

    # Compute the age in years.
    def computeAge(self):
        age = datetime.datetime.now() - self.DOB

        print(type(age))

        return age.years

    def generateID(self):
        return

    def save(self, database): # The database argument has to be a connection
        cursor = database.cursor() # Creating the cursor
        
        return

person = Person("John Doe", datetime.datetime(1980, 1, 1), 0)

print(person.age)
