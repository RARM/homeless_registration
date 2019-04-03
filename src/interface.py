from tkinter import *

def login():
    f1.pack_forget()
    f2.pack()

def search():
    f2.pack_forget()
    f3.pack()

def create():
    f2.pack_forget()
    f4.pack()

root = Tk()
root.title("Homeless Registry Login")
root.geometry("500x300")

f1 = Frame(root)  # Login frame
f2 = Frame(root)  # Search or create frame
f3 = Frame(root)  # Search form frame
f4 = Frame(root)  # Create entry frame

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


# SEARCH OR CREATE FRAME f2
f2_label_or = Label(f2, text="OR")

f2_button_search = Button(f2, text="Search for a person", command=lambda: search())
f2_button_create = Button(f2, text="Create new entry", command=lambda: create())


f2_button_search.grid(row=0)
f2_label_or.grid(row=1)
f2_button_create.grid(row=2)


#SEARCH FRAME f3
f3_label_1 = Label(f3, text="If you know the person's ID enter it, otherwise fill out the information")
f3_label_ID = Label(f3, text="ID")
f3_label_first_name = Label(f3, text="First Name")
f3_label_last_name = Label(f3, text="Last Name")
f3_label_DOB = Label(f3, text="Date of Birth")
f3_label_or = Label(f3, text="OR")

f3_entry_ID = Entry(f3)
f3_entry_first_name = Entry(f3)
f3_entry_last_name = Entry(f3)
# DROP DOWN MENU FOR DOB

f3_label_1.grid(row=0, column=1)
f3_label_ID.grid(row=1, sticky=E)
f3_label_or.grid(row=2, column=1)
f3_label_first_name.grid(row=3, column=0, sticky=E)
f3_label_last_name.grid(row=4, column=0, sticky=E)
f3_entry_ID.grid(row=1, column=1)
f3_entry_first_name.grid(row=3, column=1)
f3_entry_last_name.grid(row=4, column=1)



f3_label_ID.grid(row=0)



f1.pack()
root.mainloop()
