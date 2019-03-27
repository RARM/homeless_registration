from tkinter import *

def login():
    username = entry_1.get()
    password =

    actuauser.retrivePassword()

    if password == actualPass
    return


root = Tk()
root.title("Homeless Registry Login")
root.geometry("250x150")

label_1 = Label(root, text="Username")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root, show="*")

button_1 = Button(root, text="Login", command=login)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button_1.grid(row=2, column=1)





root.mainloop()
