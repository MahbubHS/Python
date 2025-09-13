import tkinter as tk
from tkinter import messagebox

def suggest_language():
    interests = interests_var.get()
    experience = experience_var.get()
    
    if experience == "none" or experience == "some":
        if "web" in interests:
            messagebox.showinfo("Suggestion", "Based on your interests and experience, we suggest starting with JavaScript.")
        elif "data" in interests:
            messagebox.showinfo("Suggestion", "Based on your interests and experience, we suggest starting with Python.")
        else:
            messagebox.showinfo("Suggestion", "Based on your interests and experience, we suggest starting with Python.")
    elif experience == "advanced":
        messagebox.showinfo("Suggestion", "Based on your interests and experience, we suggest starting with Python.")
    else:
        messagebox.showerror("Invalid Input", "Invalid experience level. Please enter none, some, or advanced.")

root = tk.Tk()
root.title("Programming Language Suggestion App")

interests_var = tk.StringVar(value='web development')
experience_var = tk.StringVar(value='none')

interests_label = tk.Label(root, text="What are your interests? (ex: web development, data analysis, game development) ")
interests_entry = tk.Entry(root, textvariable=interests_var)

experience_label = tk.Label(root, text="How much programming experience do you have? (none, some, advanced) ")
experience_entry = tk.Entry(root, textvariable=experience_var)

suggest_button = tk.Button(root, text="Suggest Language", command=suggest_language)

interests_label.pack()
interests_entry.pack()

experience_label.pack()
experience_entry.pack()

suggest_button.pack()

root.mainloop()
