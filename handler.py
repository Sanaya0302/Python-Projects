from tkinter import *
root=Tk()
root.geometry("100x100")
root.title("Event Handler")
def handle_keypress(event):
    print(f"Key pressed: {event.char}")
root.bind("<Key>", handle_keypress)
def handle_click(event):
    print("Button clicked!")
btn=Button(text="Click Me")
btn.pack()
btn.bind("<Button-1>", handle_click)
root.mainloop()