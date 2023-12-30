from tkinter import *

def handle_button_click(event):
    global expression_var

    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(expression_var.get())
            expression_var.set(result)
        except Exception as e:
            print(e)
            expression_var.set("Error")

    elif button_text == "C":
        expression_var.set("")
    
    else:
        expression_var.set(expression_var.get() + button_text)

def create_button(root, text, row, column, width=6, height=3, rowspan=1, columnspan=1, **kwargs):
    button = Button(root, text=text, width=width, height=height, font='lucida 12 bold', **kwargs)
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    button.bind("<Button-1>", handle_button_click)

root = Tk()
root.geometry("305x407")
root.title("Calculator")
root.configure(background='#ffffff')

# screen
expression_var = StringVar()
expression_var.set("")
screen = Entry(root, textvariable=expression_var, font="lucida 20 bold")
screen.configure(foreground='#003753')
screen.grid(row=0, column=0, columnspan=4)

button_layout = [
    ['/', '*', '-'],
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['C', '0', '.']
]

for i, row_buttons in enumerate(button_layout, start=1):
    for j, button_text in enumerate(row_buttons):
        create_button(root, button_text, i, j)

create_button(root, '+', 1, 3, height=7, rowspan=2)
create_button(root, '=', 3, 3, height=11, rowspan=3, columnspan=1, width=6, background="#fdb132", foreground="#ffffff")

root.mainloop()
