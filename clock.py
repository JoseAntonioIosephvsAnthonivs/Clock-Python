from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock Python")

def time():
    string = strftime('%HHr:%MMin:%SSeg:%p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "pink")
label.pack(anchor = 'center')
time()
mainloop()
