from datetime import datetime, date
import time

# DOB = datetime.datetime(yyyy, mm, dd)
# Using the Person class. Person('first name', 'last name', datetime.date(yyyy, mm, dd), [])
class Person:
    def __init__(self, firstName, lastName, DOB, physicalFeatures):
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = DOB
        self.physicalFeatures = physicalFeatures
        self.signInTime = time.time()
        self.age = self.computeAge()

    # Compute the age in years.
    def computeAge(self):
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))

    def generateID(self): # Generate unique ID here
        return

    def save(self, database): # The database argument has to be a connection
        cursor = database.cursor() # Creating the cursor
        result = cursor.execute()
        return result

person = Person("Mary", "Sue", date(1980, 5, 1), 0)
print(person.age)