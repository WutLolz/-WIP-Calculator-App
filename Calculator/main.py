import math
import sympy as sp
from tkinter import *
import tkinter as tk
import os

calculation = ""
power = 0
new_line = ""
bg_color = "#ffffff"
color = "#000000"

with open(file="history.txt", mode="r") as ff:
    history_list = []
    for item in ff:
        history_list.append(item.rstrip())


def add_to_calculation(symbol):
    text_result.config(state=tk.NORMAL)
    global calculation
    global power
    text = ""

    calculation += str(symbol)

    text = calculation

    if power == 1:
        power = 2
        if calculation.endswith("1"):
            text = text.replace("1", "¹")
        if calculation.endswith("2"):
            text = text.replace("2", "²")
        if calculation.endswith("3"):
            text = text.replace("3", "³")
        if calculation.endswith("4"):
            text = text.replace("4", "⁴")
        if calculation.endswith("5"):
            text = text.replace("5", "⁵")
        if calculation.endswith("6"):
            text = text.replace("6", "⁶")
        if calculation.endswith("7"):
            text = text.replace("7", "⁷")
        if calculation.endswith("8"):
            text = text.replace("8", "⁸")
        if calculation.endswith("9"):
            text = text.replace("9", "⁹")
        if calculation.endswith("0"):
            text = text.replace("0", "⁰")

    power = text.endswith("**")
    if power:
        power = 1
    text = text.replace("**", "")

    text = text.replace("*", "×")
    text = text.replace("*", "×")
    text = text.replace("/", "÷")

    text_result.delete(1.0, "end")
    text_result.insert(1.0, text)
    text_result.config(state=tk.DISABLED)


def evaluate_calculation():
    error = "Error"
    text_result.config(state=tk.NORMAL)
    global calculation
    global new_line
    global history_list
    new_line = calculation + "="
    try:
        calculation = sp.parse_expr(calculation)
        calculation = str(calculation.evalf())
        calculation = calculation.rstrip('0').rstrip('.')
        if calculation == "":
            calculation = "0"
        if calculation == "nan":
            clear_field()
            text_result.config(state=tk.NORMAL)
            text_result.insert(1.0, "Error")
            text_result.config(state=tk.DISABLED)
        elif calculation == "oo":
            clear_field()
            text_result.config(state=tk.NORMAL)
            text_result.insert(1.0, "Error")
            text_result.config(state=tk.DISABLED)
        elif calculation == "-oo":
            clear_field()
            text_result.config(state=tk.NORMAL)
            text_result.insert(1.0, "Error")
            text_result.config(state=tk.DISABLED)
        elif calculation == "zoo":
            clear_field()
            text_result.config(state=tk.NORMAL)
            text_result.insert(1.0, error)
            text_result.config(state=tk.DISABLED)
        else:
            text_result.config(state=tk.NORMAL)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
            text_result.config(state=tk.DISABLED)
    except:
        text_result.config(state=tk.NORMAL)
        clear_field()
        text_result.insert(1.0, "Error")
        text_result.config(state=tk.DISABLED)

    if calculation != "":
        new_line = new_line + calculation
    else:
        new_line = new_line + "Error"

    history = open('history.txt', 'a+')
    history.write(new_line + "\n")
    history.close()

    with open(file="history.txt", mode="r") as ff:
        history_list = []
        for item in ff:
            history_list.append(item.rstrip())


def clear_field():
    text_result.config(state=tk.NORMAL)
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.config(state=tk.DISABLED)


def clear_entry():
    global calculation
    global history_list
    for i in reversed(calculation):
        if i == "+":
            break
        elif i == "-":
            break
        elif i == "*":
            break
        elif i == "/":
            break
        else:
            calculation = calculation[:-1]
        text_result.config(state=tk.NORMAL)
        text_result.delete("end-2c")
        text_result.config(state=tk.DISABLED)


def clear_last():
    global calculation
    calculation = calculation[:-1]
    text_result.config(state=tk.NORMAL)
    text_result.delete("end-2c")
    text_result.config(state=tk.DISABLED)


def square_root():
    global calculation
    num = ""
    for i in reversed(calculation):
        if i == "+":
            break
        elif i == "-":
            break
        elif i == "*":
            break
        elif i == "/":
            break
        else:
            num = int(i)
            calculation = calculation[:-1]
        text_result.config(state=tk.NORMAL)
        text_result.delete("end-2c")
        text_result.config(state=tk.DISABLED)

        num = math.sqrt(num)
        add_to_calculation(str(num))


def clear_all():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


#Window


root = tk.Tk()
root.title("Calculator")
root.geometry("275x315")
root.iconbitmap("download.ico")

text_result = tk.Text(root, height=2, width=15, font=("Arial", 24), state=tk.DISABLED)
text_result.grid(columnspan=4, row=1)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column=1)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=6, column=0)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=6, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=3, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=4, column=3)
btn_multi = tk.Button(root, text="×", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multi.grid(row=5, column=3)
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=6, column=3)
btn_ce = tk.Button(root, text="CE", command=lambda: clear_entry(), width=5, font=("Arial", 14))
btn_ce.grid(row=2, column=0)
btn_c = tk.Button(root, text="C", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_c.grid(row=2, column=1)
btn_back = tk.Button(root, text="⌫", command=lambda: clear_last(), width=5, font=("Arial", 14))
btn_back.grid(row=2, column=3)
btn_del = tk.Button(root, text="AC", command=lambda: clear_all(), width=5, font=("Arial", 14))
btn_del.grid(row=2, column=2)
btn_equal = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=5, font=("Arial", 14))
btn_equal.grid(row=7, column=3)
btn_dec = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_dec.grid(row=7, column=0)
btn_sqr = tk.Button(root, text="√", command=lambda: square_root(), width=5, font=("Arial", 14))
btn_sqr.grid(row=7, column=1)
btn_pow = tk.Button(root, text="ₓʸ", command=lambda: add_to_calculation("**"), width=5, font=("Arial", 14))
btn_pow.grid(row=7, column=2)


def menu():
    hide_btn()
    label = Label(root, text="Menu", font=("Arial", 14))
    label.grid(row=0, column=0, pady=10)
    global hist_btn
    hist_btn = tk.Button(root, text="History", command=lambda: set_up_history(), width=10, font=("Arial", 11))
    hist_btn.grid(row=1, column=0, padx=10)
    global bg_btn
    bg_btn = tk.Button(root, text="Customize", command=lambda: custom_bg(), width=10, font=("Arial", 11))
    bg_btn.grid(row=2, column=0)


#History
def hide_btn():
    btn_1.grid_remove()
    btn_2.grid_remove()
    btn_3.grid_remove()
    btn_4.grid_remove()
    btn_5.grid_remove()
    btn_6.grid_remove()
    btn_7.grid_remove()
    btn_8.grid_remove()
    btn_9.grid_remove()
    btn_0.grid_remove()
    btn_open.grid_remove()
    btn_close.grid_remove()
    btn_plus.grid_remove()
    btn_minus.grid_remove()
    btn_multi.grid_remove()
    btn_div.grid_remove()
    btn_ce.grid_remove()
    btn_c.grid_remove()
    btn_back.grid_remove()
    btn_del.grid_remove()
    btn_equal.grid_remove()
    btn_dec.grid_remove()
    btn_sqr.grid_remove()
    btn_pow.grid_remove()
    text_result.grid_remove()
    menu_btn.grid_remove()
    try:
        hist_btn.grid_remove()
        bg_btn.grid_remove()
    except:
        pass


def show_button():
    btn_1.grid(row=3, column=0)
    btn_2.grid(row=3, column=1)
    btn_3.grid(row=3, column=2)
    btn_4.grid(row=4, column=0)
    btn_5.grid(row=4, column=1)
    btn_6.grid(row=4, column=2)
    btn_7.grid(row=5, column=0)
    btn_8.grid(row=5, column=1)
    btn_9.grid(row=5, column=2)
    btn_0.grid(row=6, column=1)
    btn_open.grid(row=6, column=0)
    btn_close.grid(row=6, column=2)
    btn_plus.grid(row=3, column=3)
    btn_minus.grid(row=4, column=3)
    btn_multi.grid(row=5, column=3)
    btn_div.grid(row=6, column=3)
    btn_ce.grid(row=2, column=0)
    btn_c.grid(row=2, column=1)
    btn_back.grid(row=2, column=3)
    btn_del.grid(row=2, column=2)
    btn_equal.grid(row=7, column=3)
    btn_dec.grid(row=7, column=0)
    btn_sqr.grid(row=7, column=1)
    btn_pow.grid(row=7, column=2)
    text_result.grid(columnspan=4, row=1)
    menu_btn.place(x=230, y=5)



def add_history_to_calc(calc, button, content_frame, label, scrollbar, canvas, frame):
    global calculation
    global text_result
    text_result.config(state=tk.NORMAL)
    calculation = calc
    for x in reversed(calc):
        if x == "=":
            calculation = calculation[:-1]
            break
        else:
            calculation = calculation[:-1]

    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    text_result.config(state=tk.DISABLED)

    button.grid_remove()
    content_frame.grid_remove()
    label.grid_remove()
    scrollbar.grid_remove()
    canvas.grid_remove()
    frame.grid_remove()
    show_button()


def set_up_history():
    # Step 3: Create a Frame for Grid Layout
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    # Step 4: Create a Canvas and Scrollbar
    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Step 5: Create a Frame for Scrollable Content
    content_frame = tk.Frame(canvas)

    # Step 6: Configure the Canvas and Scrollable Content Frame
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Step 7: Add Widgets to the Content Frame
    # Example widgets (replace with your own)
    label = tk.Label(content_frame, text="History", font=("Arial", 14))
    label.grid(row=0, column=0)

    count = 0

    history_list.reverse()

    for i in history_list:
        count += 1
        button = tk.Button(content_frame, text=f"{i}",
                           command=lambda i=i: add_history_to_calc(i, button, content_frame, label, scrollbar, canvas, frame), width=15, font=("Arial", 12))
        button.grid(row=count, column=0, pady=2)

    # Step 8: Create Window Resizing Configuration
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    # Step 9: Pack Widgets onto the Window
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Step 10: Bind the Canvas to Mousewheel Events
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    hide_btn()


#Customize background
def set_color(colour, btn_white, btn_gry, btn_red, btn_ylw, btn_orng, btn_grn, btn_blu, btn_pnk, label):
    global color
    global bg_color
    if colour == "white":
        bg_color = "#ffffff"
        color = "#000000"
    if colour == "pink":
        bg_color = "#dd00ff"
    btn_white.grid_remove()
    btn_gry.grid_remove()
    btn_red.grid_remove()
    btn_ylw.grid_remove()
    btn_orng.grid_remove()
    btn_grn.grid_remove()
    btn_blu.grid_remove()
    btn_pnk.grid_remove()
    label.grid_remove()
    show_button()


def custom_bg():
    hide_btn()
    label = tk.Label(root, text="Background color", font=("Arial", 14))
    label.grid(row=0, column=0, pady=5)
    btn_white = tk.Button(root, text="White", width=7, font=("Arial", 12), bg='#ffffff')
    btn_white.grid(row=1, column=0, pady=5)
    btn_gry = tk.Button(root, text="Dark", width=7, font=("Arial", 12), bg='#252526', fg='#ffffff')
    btn_gry.grid(row=1, column=1, pady=5)
    btn_red = tk.Button(root, text="Red", width=7, font=("Arial", 12), bg='#f22416')
    btn_red.grid(row=2, column=0, pady=5)
    btn_ylw = tk.Button(root, text="Yellow", width=7, font=("Arial", 12), bg='#f7ec19')
    btn_ylw.grid(row=2, column=1, pady=5)
    btn_orng = tk.Button(root, text="Orange", width=7, font=("Arial", 12), bg='#ffa500')
    btn_orng.grid(row=3, column=0, pady=5)
    btn_grn = tk.Button(root, text="Green", width=7, font=("Arial", 12), bg='#1adb1a')
    btn_grn.grid(row=3, column=1, pady=5)
    btn_blu = tk.Button(root, text="Blue", width=7, font=("Arial", 12), bg='#00b3ff')
    btn_blu.grid(row=4, column=0, pady=5)
    btn_pnk = tk.Button(root, text="Pink", command=lambda: set_color("pink", btn_white, btn_gry, btn_red, btn_ylw, btn_orng, btn_grn, btn_blu, btn_pnk, label), width=7, font=("Arial", 12), bg='#dd00ff')
    btn_pnk.grid(row=4, column=1, pady=5)


menu_btn = tk.Button(root, text="🏠", command=lambda: menu(), width=3, font=("Arial", 11))
menu_btn.place(x=230, y=5)

root.mainloop()
