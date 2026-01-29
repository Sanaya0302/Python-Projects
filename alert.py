from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def show_alert():
    messagebox.showwarning("alert", "STOP! Virus detected!")
btn=Button(root, text="Scan Virus", command=show_alert)
btn.place(x=40, y=80)
root.mainloop()