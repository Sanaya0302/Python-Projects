from locale import currency
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
        for i,(item,price) in enumerate(self.menu.items(),start=1):
            label=ttk.Label(frame,text=f"{item.capitalize()} (${price})")
            label.grid(row=i,column=0,pady=5,padx=10)
            self.menu_label[item]=label
            quantity=ttk.Entry(frame,width=5)
            quantity.grid(row=i,column=1,pady=5,padx=10)
            self.menu_quantity[item]=quantity
        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Select Currency:").grid(row=i+1,column=0,pady=5,padx=10)
        currency_dropdown=ttk.Combobox(frame,width=18,textvariable=self.currency_var,values=["USD","INR"],state="readonly")
        currency_dropdown.grid(row=i+1,column=1,pady=5,padx=10)
        currency_dropdown.current(1)
        self.currency_var.trace("w",self.update_menu_prices)
        order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=i+2,columnspan=3,pady=10,padx=10)
    def setup_background(self,root):
        bg_width,bg_height=800,600
        canvas=ttk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()
        original_image=tk.PhotoImage(file="restaurant.jpeg")
        bg=original_image.subsample(original_image.width()//bg_width,original_image.height()//bg_height)
        canvas.create_image(0,0,image=bg,anchor=tk.NW)
        canvas.image=bg
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_label.items():
            price = self.menu[item] * rate
            label.config(text=f"{item.capitalize()} ({symbol}{price:.2f})") 
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
    for item, entry in self.menu_quantity.items():
        quantity = entry.get()
        if quantity.isdigit():
            quantity = int(quantity)
            price = self.menu[item] * rate
            cost = quantity * price
            total_cost += cost

            if quantity > 0:
                order_summary += (
                    f"{item}: {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n")
    if total_cost > 0:
        order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
        messagebox.showinfo("Order Placed", order_summary)
    else:
        messagebox.showerror(
            "Error",
            "Please order at least one item.")
    if __name__ == "__main__":
        root = tk.Tk()
        app = RestaurantApp(root)
        root.geometry("800x600")  
        root.mainloop() 

