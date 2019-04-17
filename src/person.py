from datetime import datetime, date
import time
import random
import sqlite3

# Using the Person class. Person('first name', 'last name', [yyyy, mm, dd], ["Height", "Weight", "Eyes color", "Hair color", "Gender"], ethnicity)
class Person:
    def __init__(self, firstName, lastName, DOB, physicalFeatures, ethnicity, uniqueID=NULL, signInTime=time.time()): # Constructor
        # Settings
        self.separatorStr = '~' # Separator for list to strings in database

        # Class variables from arguments
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = date(DOB[0], DOB[1], DOB[2]) # DOB = date(yyyy, mm, dd)
        self.physicalFeatures = physicalFeatures
        self.ethnicity = ethnicity
        self.signInTime = signInTime

        # Variables calculated with the class methods
        self.DOB_String = self.dateToString(DOB[0], DOB[1], DOB[2])
        self.age = self.computeAge()
        self.physicalFeatures_String = self.stringFromList(physicalFeatures)

        if uniqueID = NULL:
            self.uniqueID = self.generateID()
        else:
            self.uniqueID = uniqueID



    # Methods below ----------
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

    @staticmethod
    def hairColorTest(hairColor): # hairColorTest: return true if argument is a valid hair color
        flag = False
        hairColor = [""] * (10)

        # List of valid hair colors
        hairColor[0] = "Orange"
        hairColor[1] = "Blue"
        hairColor[2] = "Black"
        hairColor[3] = "Brown"
        hairColor[4] = "Blonde"
        hairColor[5] = "Green"
        hairColor[6] = "Yellow"
        hairColor[7] = "Red"
        hairColor[8] = "Dyed"
        hairColor[9] = "Grey"

        color = hairColor
        
        for index in range(0, 9 + 1, 1):
            if color == hairColor[index]:
                flag = True
        return flag


# Test block
person1 = Person("Mary", "Sue", [1980, 5, 1], ["5'1", "120", "Blue", "Brown", "Female"], "White")
print(person1.uniqueID)


# Joseph eye color test
index = 0
eyeColor = [""] * (8)

eyeColor[0] = "Blue"
eyeColor[1] = "Green"
eyeColor[2] = "Red"
eyeColor[3] = "Orange"
eyeColor[4] = "Black"
eyeColor[5] = "Grey"
eyeColor[6] = "Brown"
eyeColor[7] = "Hazel"
flag = False
print("what is the eye color?")
color = input()
for index in range(0, 7 + 1, 1):
    if eyeColor[index] == color:
        flag = True
if flag == True:
    print("The color exist")
else:
    print("Not an Eye Color")
    
index = 0
flag = False
gender = [""] * (2)

gender[0] = "Male"
gender[1] = "Female"
print("what is the Gender?")
personsGender = input()
for index in range(0, 1 + 1, 1):
    if gender[index] == personsGender:
        flag = True
if flag == True:
    print("The Gender is?" + personsGender)
else:
    print("Not a gender")

index = 0
flag = False
ethnicity = [""] * (4)

ethnicity[0] = "White"
ethnicity[1] = "Spanish"
ethnicity[2] = "African American"
ethnicity[3] = "Alaskin"
print("what is the Ethnicity?")
personsEthnicity = input()
for index in range(0, 3 + 1, 1):
    if ethnicity[index] == personsEthnicity:
        flag = True
if flag == True:
    print("The Persons Ethnicity is?" + personsEthnicity)
else:
    print("Not a Ethnic Background")
