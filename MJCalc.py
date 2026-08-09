import tkinter as tk
from tkinter import messagebox

num1 = ""
num2 = ""
oper = ""


def button_pressed(text):
    global num1, num2, oper

    if text == "=":
        calculate()
    elif text == "C":
        num1 = ""
        num2 = ""
        oper = ""
    elif text in ["+", "-", "×", "÷"]:
        oper = text
    elif oper == "":
        num1 += str(text)
    else:
        num2 += str(text)


def calculate():
    global num1, num2, oper

    if num1 == "" or num2 == "":
        messagebox.showerror("Error", "Enter two numbers first!")
        return

    if oper == "+":
        result = int(num1) + int(num2)

    elif oper == "-":
        result = int(num1) - int(num2)

    elif oper == "×":
        result = int(num1) * int(num2)

    elif oper == "÷":
        if num2 == "0":
            messagebox.showerror(
                "Error",
                "You can't divide by 0, idiot. Did you pay attention during math!???????????????????????"
            )
            return

        result = int(num1) / int(num2)

    else:
        return

    messagebox.showinfo("Result", f"Result: {result}")

    num1 = ""
    num2 = ""
    oper = ""


root = tk.Tk()
root.title("MJCalc")
root.geometry("400x400")
root.configure(bg="black")

buttons = [
    "7", "8", "9", "÷",
    "4", "5", "6", "×",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

for i, text in enumerate(buttons):
    row = i // 4
    column = i % 4

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 32),
        command=lambda t=text: button_pressed(t)
    )
    button.grid(row=row, column=column, sticky="nsew")


for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()