def checkPassword(userName, passWord):
    actualUsername = "Admin"
    actualPassword = "Admin"
    if userName == actualUsername:
        if passWord == actualPassword:
            checkPassword = True
        else:
            checkPassword = False
    else:
        checkPassword = False
    
    return checkPassword

# Main
userName = "Admin"
passWord = "Admin"
print("What is the username?")
passWord = input()
print("what is the password?")
passWord = input()
test = checkPassword(userName, passWord)
if test == True:
    print("Login successful")
else:
    print("Login not successful")
