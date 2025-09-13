import tkinter as tk
from tkinter import messagebox

def show_channels():
    choice = var.get()
    if choice == 1:
        messagebox.showinfo("Best YouTube Channels", "1. Code with Mosh\n2. Traversy Media\n3. FreeCodeCamp.org")
    elif choice == 2:
        messagebox.showinfo("Best YouTube Channels", "1. Corey Schafer\n2. Sentdex\n3. Coding Tech")
    elif choice == 3:
        messagebox.showinfo("Best YouTube Channels", "1. LearnCode.academy\n2. Derek Banas\n3. Programming with Mosh")

root = tk.Tk()
root.title("Learn Programming")

instruction_label = tk.Label(root, text="Choose your preferred programming language:")
instruction_label.pack()

var = tk.IntVar()
python_button = tk.Radiobutton(root, text="Python", variable=var, value=1)
python_button.pack()

javascript_button = tk.Radiobutton(root, text="Javascript", variable=var, value=2)
javascript_button.pack()

java_button = tk.Radiobutton(root, text="Java", variable=var, value=3)
java_button.pack()

find_channels_button = tk.Button(root, text="Find Channels", command=show_channels)
find_channels_button.pack()

root.mainloop()
