from datetime import datetime, date
import time
import random

# Using the Person class. Person('first name', 'last name', [yyyy, mm, dd]], ["Height", "Weight", "Eyes color", "Hair color", "Gender"], ethnicity)
class Person:
    def __init__(self, firstName, lastName, DOB, physicalFeatures, ethnicity): # Constructor
        self.uniqueID = self.generateID()
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = date(DOB[0], DOB[1], DOB[2]) # DOB = date(yyyy, mm, dd)
        self.DOB_String = self.dateToString(DOB[0], DOB[1], DOB[2])
        self.physicalFeatures = physicalFeatures
        # self.physicalFeatures_String = self.getStringOfList(physicalFeatures)
        self.signInTime = time.time()
        self.age = self.computeAge()
        self.ethnicity = ethnicity


#    def dateToString(self, yyyy, mm, dd): # Convert the DOB object to a
#        # Converting the month to a string of two character
#        if len(str(mm)) == 1:
#            month = "0" + str(mm)
#        elif len(str(mm)) == 2:
#            month =  str(mm)
#        else:
#            month = "00"
#            print("An error has occured creating the string for DOB...")
#
#        # Converting the day to a string of two characters
#        if len(str(dd)) == 1:
#            day = "0" + str(dd)
#        elif len(str(dd)) == 2:
#            day = str(dd)
#        else:
#            day = "00"
#            print("An error has occcured creating the string for DOB...")
#
#        return str(yyyy) + month + day


    def computeAge(self): # Compute the age in years
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))


    def generateID(self): # Generate unique ID here
      randomNumber = str(random.randint(100, 999))
      initials = self.firstName[0] + self.lastName[0]
      DOB = str(int(self.DOB.year) + int(self.DOB.month) + int(self.DOB.day))[3]
      return randomNumber + initials + DOB


    def save(self, database): # The database argument has to be a connection
        cursor = database.cursor() # Creating the cursor
        result = cursor.execute()
        content = [(self.firstName, self.lastName, self.DOB_String, self.physicalFeatures),]
        result = cursor.execute("INSERT INTO people VALUES (?, ?, ?, ?)", content)
        return result


    @classmethod
    def retrievePerson(myCls, ID):
        return myCls(firstName, lastName, DOB, physicalFeatures, ethnicity)

    @staticmethod
    def retrieveList(ID, firstN, lastN, [yyyy, mm, dd])
        return list


# Test area
person1 = Person("Mary", "Sue", [1980, 5, 1], 0)
print(person1.age)
print(person1.DOB)
print(person1.DOB_String)
print(person1.generateID())
