from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("Money Counter")
root.geometry("650x400")
root.configure(bg="lightblue")
upload=Image.open("oney.jpeg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg="lightblue")
label.place(x=180,y=20)
Label1=Label(root,text="Hey user,Welcome to Money Counter!",bg="lightblue")
Label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    Msgbox=messagebox.showinfo("Alert","Do you want to calculate to denominations?")
    if Msgbox=="ok":
        topwin()
button1=Button(root,text="Click here to start",command=msg,bg="cyan",fg="black")
button1.place(x=260,y=360,anchor=CENTER)
def topwin():
    top=Toplevel()
    top.title("Money Counter")
    top.geometry("600x350+50+50")
    top.configure(bg="lavender")
    Label2=Label(top,text="Enter the amount you want to count",bg="lavender")
    entry1=Entry(top)
    Label3=Label(top,text="Here is the breakdown of denominations:",bg="lavender")
    L1=Label(top,text="2000",bg="lavender")
    L2=Label(top,text="500",bg="lavender")
    L3=Label(top,text="100",bg="lavender")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculate():
        try:
            amount=int(entry1.get())
            note2000=amount//2000
            amount=amount%2000
            note500=amount//500
            amount=amount%500
            note100=amount//100
            t1.delete(0,END)
            t2.delete(0,END)    
            t3.delete(0,END)
            t1.insert(END,note2000)
            t2.insert(END,note500)
            t3.insert(END,note100)
        except ValueError:
            messagebox.showerror("Invalid input","Please enter a valid integer amount.")
    btn=Button(top,text="Calculate",command=calculate,bg="cyan",fg="black")
    Label2.place(x=230,y=50)
    btn.place(x=240,y=120)
    entry1.place(x=200,y=80)
    Label3.place(x=140,y=170)
    L1.place(x=180,y=200)
    L2.place(x=180,y=230)
    L3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()