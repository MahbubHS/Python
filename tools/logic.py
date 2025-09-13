import tkinter as tk

def check_answer():
    user_input = input_box.get()
    if user_input == "x < y and y > 0":
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect. Try again.")

root = tk.Tk()
root.title("Logic Builder")

instruction_label = tk.Label(root, text="Enter the logical expression that evaluates to True:")
instruction_label.pack()

input_box = tk.Entry(root)
input_box.pack()

submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
