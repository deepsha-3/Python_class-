import tkinter as tk 
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x500")

label = tk.Label(root, text="Hello,world!", font=("Arial",24))
label.pack()

def say_hello():
 print("Button clicked!")
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()