from tkinter import *
import os


def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()


def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text="Welcome to Dashboard").pack()
    Button(screen8, text = "Create Note").pack()
    Button(screen8, text = "View Note").pack()
    Button(screen8, text = "Delete Note").pack()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Sucess")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Sucess").pack()
    Button(screen3, text ="OK", command = delete2).pack()

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Sucess")
    screen4.geometry("150x100")
    Label(screen4, text = "Wrong Password").pack()
    Button(screen4, text ="OK", command = delete3).pack()

def User_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Sucess")
    screen5.geometry("150x100")
    Label(screen5, text = "No user found").pack()
    Button(screen5, text ="OK", command = delete4).pack()

#new funtion for register button
def register_user():

    username_info = username.get()     #to get username details
    password_info = password.get()     #to get password details

    #to enter values in text files
    file=open(username_info, "w")
    file.write(username_info+"\n")           
    file.write(password_info)
    file.close()

    #to clear the field once user registerd succesfully
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    #to tell user registration succesfull
    Label(screen1, text = "Successfully Registered",fg = "Green",font = ("Times new roman",11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file = open(username1, "r")
        verify = file.read().splitlines()       #read all lines within text files and ignore all blank space
        if password1 in verify:
           login_sucess()
        else:
            password_not_recognized()
    else:
        User_not_found()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    

    #to define variables outside the fuction we globalies entries
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    global username_entry
    global password_entry
    username_entry = Entry(screen1, textvariable = username)        #to store values in stringvariable
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()                         #to give space between lines
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
    

def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height=1,command=login_verify).pack()
    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Library Management System")
    Label(text = "Library Management System", bg = "white",fg="#427bff",width="300",height="2", font = ("Times New Roman",43, "bold")).pack()
    Label(text = "").pack()
    Button(text = "Login",height = "2", width = "30", command = Login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    screen.mainloop()

main_screen()
