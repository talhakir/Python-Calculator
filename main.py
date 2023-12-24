from tkinter import *

expression = ""

# For Total
history_setT = []
history_setT.clear()

# For Expression
history_setE = []
history_setE.clear()


# Equal sign
def e_press():
    global expression

    # Sure to handle error
    try:

        # Display the result
        total = str(eval(expression))

        history_setT.append(total)
        history_setE.append(expression)

        equation.set(total)

        expression = ""

    except:
        equation.set(" error")
        expression = ""


def press(number):
    global expression

    expression = expression + str(number)

    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


# Collect history and show
def history():
    history_window = Toplevel(c_gui)

    history_window.title("History")

    history_window.configure(background="light blue")

    history_window.geometry("200x200")

    # Printing each total and expression
    for i in range(len(history_setT)):
        Label(history_window, text=f"{history_setE[i]}: {history_setT[i]}", fg="brown", bg="light blue").pack()


if __name__ == "__main__":
    c_gui = Tk()

    c_gui.configure(background="light blue")

    c_gui.title("First Calculator")

    c_gui.geometry("270x350")

    equation = StringVar()

    expression_field = Entry(c_gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    # b_ => button_
    b1 = Button(c_gui, text=' 1 ', fg='black', bg='light green',
                command=lambda: press(1), height=2, width=7)
    b1.grid(row=2, column=0, padx=2, pady=5)

    b2 = Button(c_gui, text=' 2 ', fg='black', bg='light green',
                command=lambda: press(2), height=2, width=7)
    b2.grid(row=2, column=1, padx=2, pady=5)

    b3 = Button(c_gui, text=' 3 ', fg='black', bg='light green',
                command=lambda: press(3), height=2, width=7)
    b3.grid(row=2, column=2, padx=2, pady=5)

    minus = Button(c_gui, text='-', fg='white', bg='brown',
                   command=lambda: press("-"), height=2, width=7)
    minus.grid(row=2, column=3, padx=2, pady=5)

    b4 = Button(c_gui, text=' 4 ', fg='black', bg='light green',
                command=lambda: press(4), height=2, width=7)
    b4.grid(row=3, column=0, padx=2, pady=2)

    b5 = Button(c_gui, text=' 5 ', fg='black', bg='light green',
                command=lambda: press(5), height=2, width=7)
    b5.grid(row=3, column=1, padx=2, pady=2)

    b6 = Button(c_gui, text=' 6 ', fg='black', bg='light green',
                command=lambda: press(6), height=2, width=7)
    b6.grid(row=3, column=2, padx=2, pady=2)

    plus = Button(c_gui, text='+', fg='white', bg='brown',
                  command=lambda: press("+"), height=2, width=7)
    plus.grid(row=3, column=3, padx=2, pady=2)

    b7 = Button(c_gui, text='7', fg='black', bg='light green',
                command=lambda: press(7), height=2, width=7)
    b7.grid(row=4, column=0, padx=2, pady=2)

    b8 = Button(c_gui, text='8', fg='black', bg='light green',
                command=lambda: press(8), height=2, width=7)
    b8.grid(row=4, column=1, padx=2, pady=2)

    b9 = Button(c_gui, text='9', fg='black', bg='light green',
                command=lambda: press(9), height=2, width=7)
    b9.grid(row=4, column=2, padx=2, pady=2)

    multiply = Button(c_gui, text='*', fg='white', bg='brown',
                      command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=4, column=3, padx=2, pady=2)

    b0 = Button(c_gui, text='0', fg='black', bg='light green',
                command=lambda: press(0), height=2, width=7)
    b0.grid(row=5, column=0, padx=2, pady=2)

    right_parenthesis = Button(c_gui, text=" ( ", fg="black", bg="light green",
                               command=lambda: press(" ( "), height=2, width=7)
    right_parenthesis.grid(row=5, column=1, padx=2, pady=2)

    left_parenthesis = Button(c_gui, text=" ) ", fg="black", bg="light green",
                              command=lambda: press(" ) "), height=2, width=7)
    left_parenthesis.grid(row=5, column=2, padx=2, pady=2)

    divide = Button(c_gui, text='/', fg='white', bg='brown',
                    command=lambda: press("/"), height=2, width=7)
    divide.grid(row=5, column=3, padx=2, pady=2)

    point = Button(c_gui, text='.', fg='black', bg='light green',
                   command=lambda: press('.'), height=2, width=7)
    point.grid(row=6, column=0, padx=2, pady=2)

    clear = Button(c_gui, text='C', fg='white', bg='brown',
                   command=clear, height=2, width=7)
    clear.grid(row=6, column=1, padx=2, pady=2)

    equal = Button(c_gui, text='=', fg='white', bg='brown',
                   command=e_press, height=2, width=7)
    equal.grid(row=6, column=2, padx=2, pady=2)

    history = Button(c_gui, text='H', fg='black', bg='grey',
                     command=history, height=2, width=7)
    history.grid(row=6, column=3, padx=2, pady=2)

    c_gui.mainloop()
