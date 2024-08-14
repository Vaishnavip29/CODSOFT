
#tASK 3 : PASSWORD GENERATOR
from tkinter import *
import string
import random

root = Tk()
root.configure(background="white")
root.title("Password Generator")
root.geometry("500x400")  
root.resizable(False, False)

passstr = StringVar()
pwd_len = IntVar()

def get_pass():
    try:
        length = pwd_len.get()
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        pass1 = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(pass1) for _ in range(length))
        passstr.set(password)
    except ValueError as e:
        passstr.set(str(e))

def copy_to_clipboard():
    
    root.clipboard_clear()
    root.clipboard_append(passstr.get())
    root.update()  


Label(root, text="Password Generator", font="calibri 28 bold", background="white").pack(pady=10)

Label(root, text="Enter Length Of Password :", font="calibri 15 ", background="white").pack(pady=5)

length_entry = Entry(root, textvariable=pwd_len, font="calibri 12")
length_entry.pack(pady=5)

Button(root, text="Generate Password", command=get_pass, font="calibri 15",background="white").pack(pady=10)

password_entry = Entry(root, textvariable=passstr, state='readonly', font="calibri 15", width=30)
password_entry.pack(pady=5)

Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font="calibri 15").pack(pady=10)


root.mainloop()
