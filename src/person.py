from datetime import datetime, date
import time
import random
import sqlite3

# Using the Person class. Person('first name', 'last name', [yyyy, mm, dd], ["Height", "Weight", "Eyes color", "Hair color", "Gender"], ethnicity)
class Person:
    def __init__(self, firstName, lastName, DOB, physicalFeatures, ethnicity): # Constructor
        self.uniqueID = self.generateID()
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = date(DOB[0], DOB[1], DOB[2]) # DOB = date(yyyy, mm, dd)
        self.DOB_String = self.dateToString(DOB[0], DOB[1], DOB[2])
        self.physicalFeatures = physicalFeatures
        self.physicalFeatures_String = self.stringFromList(physicalFeatures)
        self.signInTime = time.time()
        self.age = self.computeAge()
        self.ethnicity = ethnicity

        # Separator for list to strings in database
        self.separatorStr = '~'


    def computeAge(self): # Compute the age in years
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))


    def generateID(self): # Generate unique ID here
      randomNumber = str(random.randint(100, 999))
      initials = self.firstName[0] + self.lastName[0]
      DOB = str(int(self.DOB.year) + int(self.DOB.month) + int(self.DOB.day))[3]
      return randomNumber + initials + DOB


    def stringFromList(self, my_list):
        resultant_string = my_list.split(self.separatorStr)
        return resultant_string


    def save(self, database): # The database argument has to be a connection
        cursor = database.cursor() # Creating the cursor
        result = cursor.execute()
        content = [(self.firstName, self.lastName, self.DOB_String, self.physicalFeatures_String, self.ethnicity),]
        result = cursor.execute("INSERT INTO people VALUES (?, ?, ?, ?, ?)", content)
        return result


#    @classmethod
#    def retrieve(myCls, ID, database_name): # Person.retrieve(ID, database_name): Creates a person object based on a database info. The database should match the data as in the Person.save() method
        # Creating cursor
#        cursor = database.cursor()
#        return myCls(firstName, lastName, DOB, physicalFeatures, ethnicity)

#    @staticmethod
#    def retrieveList(ID, firstN, lastN, [yyyy, mm, dd])
#        return list


# Test area
person1 = Person("Mary", "Sue", [1980, 5, 1], ["5'1", "120", "Blue", "Brown", "Female"], "White")
