import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.menu={
            "fries":2,
            "lunch meal":2,
            "pizza meal":4,
            "burger meal":3,
            "cheese burger meal":2.5,
            "drinks":1
        }
        self.exchange_rate=82
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Welcome to the Restaurant!",font=("Arial",20,"bold")).grid(row=0,columnspan=2,pady=10,padx=10)
        self.menu_label={}
        self.menu_quantity={}
        