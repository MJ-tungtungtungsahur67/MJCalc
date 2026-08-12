import tkinter as tk
from tkinter import messagebox

num1 = ""
num2 = ""
oper = ""
result = ""
def block_typing(event):
    return "break"


def add_to_expression(value):
    expression.insert(tk.END, str(value))

def button_pressed(text):
    global num1, num2, oper, result

    if text == "=":
        calculate()
    elif text == "C":
        num1 = ""
        num2 = ""
        oper = ""
        expression.delete(0, tk.END)
    elif text == "E":
        if expression.get() != "":
            if oper == "":
                num1 = num1[:-1]
            else:
                num2 = num2[:-1]
        expression.delete(expression.index(tk.END) - 1)
    elif text == ".":
        if oper == "":
            if "." not in num1:
                num1 += "."
                add_to_expression(".")
        else:
            if "." not in num2:
                num2 += "."
                add_to_expression(".")
    elif text.isdigit():
        if oper == "":
            num1 += str(text)
            add_to_expression(text)
        else:
            num2 += str(text)
            add_to_expression(text)

            
    elif text == "ans":
        if result == "":
           messagebox.showerror("ERROR", "YOU NEVER HAD A PREVIOUS ANSWER, YOU IDIOT!") 
        elif oper == "":
            num1 = str(result)
            add_to_expression(result)
        else:
            num2 = str(result)
            add_to_expression(result)
    elif text in ["+", "-", "×", "÷", "%"]:
        oper = text
        add_to_expression(text)
    elif oper == "":
        num1 += str(text)
        add_to_expression(text)
    else:
        num2 += str(text)
        add_to_expression(text)


def calculate():
    global num1, num2, oper, result

    if oper == "%":
        if num1 == "":
            messagebox.showerror("Error", "Enter a number first!")
            return

        result = float(num1) / 100

    elif num1 == "" or num2 == "":
        messagebox.showerror("Error", "Enter two numbers first!")
        return

    elif oper == "+":
        result = float(num1) + float(num2)

    elif oper == "-":
        result = float(num1) - float(num2)

    elif oper == "×":
        result = float(num1) * float(num2)

    elif oper == "÷":
        if num2 == "0":
            messagebox.showerror(
                "Error",
                "You can't divide by 0, idiot. Did you pay attention during math!???????????????????????"
            )
            return

        result = float(num1) / float(num2)

    else:
        return

    expression.delete(0, tk.END)

    expression.insert(tk.END, result)
 
    messagebox.showinfo("Result", f"Result: {result}")

    num1 = str(result)
    num2 = ""
    oper = ""


root = tk.Tk()
root.title("MJCalc")
root.geometry("400x400")
root.configure(bg="#000000")

buttons = [
    "7", "8", "9", "÷",
    "4", "5", "6", "×",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
    "ans","E", ".", "%"
]

for i, text in enumerate(buttons):
    row = i // 4
    column = i % 4

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 32),
        bg="#222222",
        fg="#FFFFFF",
        command=lambda t=text: button_pressed(t)
    )
    button.grid(row=row, column=column, sticky="nsew")

expression = tk.Entry(root, font=("Arial", 32), bg="#000000", fg="#FFFFFF", insertbackground="#FFFFFF")
expression.bind("<Key>", block_typing)
expression.grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
   

for i in range(4):
 root.grid_columnconfigure(i, weight=1)
root.mainloop()