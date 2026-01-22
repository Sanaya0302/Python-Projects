from tkinter import *
import tkinter as tk
from datetime import date
win=Tk()
win.geometry("400x400")
win.title("Widgets!!!!")
lab=Label(text="Welcome to Tkinter Widgets",fg="white",bg="cyan",font=("Arial",16),height=1,width=300)
lab2=Label(text="Name please",bg="yellow")     
name=Entry()
def display():
    name1=name.get()
    global Message
    Message="Welcome to my application\n Today's date is " 
    greet="Hello"+" "+name1+"\n"
    Textbox.insert(END,greet)
    Textbox.insert(END,Message)
    Textbox.insert(END,date.today())
Textbox=Text(height=3)
btn=Button(text="begin",bg="lightgreen",command=display,height=1)
lab.pack()
lab2.pack()
name.pack()
btn.pack()
Textbox.pack()
win.mainloop()