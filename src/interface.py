from tkinter import *

def menu_return1():
    f3_1.pack_forget()
    f3_2.pack_forget()
    f2_2.pack()
    f2_1.pack()

def menu_return2():
    f5.pack_forget()
    f5.pack_forget()
    f2_2.pack()
    f2_1.pack()


def login():
    f1.pack_forget()
    f2_2.pack()
    f2_1.pack()


def search():
    f2_1.pack_forget()
    f2_2.pack_forget()
    f3_1.pack()
    f3_2.pack()


def create():
    f2_1.pack_forget()
    f4.pack()

def submit_search(day_var, month_var, year_var):
    test_months = ["September", "April", "June", "November"]
    if month_var == "February" and day_var > 28:
        if day_var != 29:
            print("Error: February only has 28 days or 29 on a leap year")
        elif day_var == 29 and year_var % 4 != 0:
            print("Error: " + str(year_var) + " is not a leap year")
        else:
            print("Date of birth accepted")
            f3_1.pack_forget()
            f3_2.pack_forget()
            f5.pack()
    elif day_var == 31 and month_var in test_months:
        print("Error: " + month_var + " does not have 31 days")
    else:
        print("Date of birth accepted")
        f3_1.pack_forget()
        f3_2.pack_forget()
        f5.pack()


resultsList = ["John", "Connor", "Joe", "Sam", "Bill"]

root = Tk()
root.title("Homeless Registry")
root.geometry("500x300")

f1 = Frame(root)  # Login frame
f2_1 = Frame(root)  # Search or create frame
f2_2 = Frame(root, height=65)  # Search or create frame buffer
f3_1 = Frame(root)  # Search form frame 1
f3_2 = Frame(root)  # Search form frame 2
f4 = Frame(root)  # Create entry frame
f5 = Frame(root)  # Search returns

# LOGIN FRAME f1
f1_label_username = Label(f1, text="Username")
f1_label_password = Label(f1, text="Password")

f1_entry_username = Entry(f1)
f1_entry_password = Entry(f1, show="*")

f1_button_login = Button(f1, text="Login", command=lambda: login())

f1_label_username.grid(row=0, sticky=E, pady=20)
f1_label_password.grid(row=1, sticky=E)
f1_entry_username.grid(row=0, column=1)
f1_entry_password.grid(row=1, column=1)
f1_button_login.grid(row=2, column=1, pady=20)


# SEARCH OR CREATE FRAME f2_1
f2_label_or = Label(f2_1, text="OR")

f2_button_search = Button(f2_1, text="Search for a person", command=lambda: search())
f2_button_create = Button(f2_1, text="Create new entry", command=lambda: create())


f2_button_search.grid(row=0)
f2_label_or.grid(row=1)
f2_button_create.grid(row=2)


#SEARCH FRAME f3
day_var = IntVar(f3_2)
day_var.set(1)
month_var = StringVar(f3_2)
month_var.set("January")
year_var = IntVar(f3_2)
year_var.set(2019)

f3_label_1 = Label(f3_1, text="If you know the person's ID enter it, otherwise fill out the information")
f3_label_ID = Label(f3_1, text="ID")
f3_label_first_name = Label(f3_1, text="First Name")
f3_label_last_name = Label(f3_1, text="Last Name")
f3_label_DOB = Label(f3_2, text="Date of Birth")
f3_label_or = Label(f3_1, text="OR")


f3_entry_ID = Entry(f3_1)
f3_entry_first_name = Entry(f3_1)
f3_entry_last_name = Entry(f3_1)

# DROP DOWN MENU FOR DOB
dayChoices = []
for i in range(1, 32, 1):
    dayChoices.append(i)
f3_day_dropdown = OptionMenu(f3_2, day_var, *dayChoices)

monthChoices = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
f3_month_dropdown = OptionMenu(f3_2, month_var, *monthChoices)

yearChoices = []
for i in range(1920, 2020, 1):
    yearChoices.append(i)
f3_year_dropdown = OptionMenu(f3_2, year_var, *yearChoices)

f3_button_submit = Button(f3_2, text="Submit", command=lambda: submit_search(day_var.get(), month_var.get(), year_var.get()))
f3_back_to_menu = Button(f3_1, text="<-- Main Menu", command=lambda: menu_return1())

f3_back_to_menu.grid(row=0)


f3_label_DOB.grid(row=2)
f3_day_dropdown.grid(row=2, column=1)
f3_month_dropdown.grid(row=2, column=2)
f3_year_dropdown.grid(row=2, column=3)
f3_button_submit.grid(row=3, column=2)

f3_label_1.grid(row=0, column=1)
f3_label_ID.grid(row=1, column=0, sticky=E)
f3_label_or.grid(row=2, column=1)
f3_label_first_name.grid(row=3, column=0, sticky=E)
f3_label_last_name.grid(row=4, column=0, sticky=E)
f3_entry_ID.grid(row=1, column=1)
f3_entry_first_name.grid(row=3, column=1)
f3_entry_last_name.grid(row=4, column=1)

# SEARCH RETURNS
f5_back_to_menu = Button(f5, text="<-- Main Menu", command=lambda: menu_return2())
resultsTable = Listbox(f5, font="ansifixed")

maxChar = len(resultsList[0])
for i in resultsList:
    if len(i) > maxChar:
        maxChar = len(i)
for i in resultsList:
    while len(i) < maxChar:
        i += "0"
    resultsTable.insert(END, i)
    print(maxChar)

resultsTable.grid(row=1)
f5_back_to_menu.grid(row=0)





f1.pack()
root.mainloop()
