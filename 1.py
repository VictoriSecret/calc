from customtkinter import *
from PIL import Image

#Проверка изменений


def add_digit(digit):
    value = entry_formula.get() + str(digit)
    entry_formula.delete(0, END)
    entry_formula.insert(0, value)

def add_operation(operation):
    value = entry_formula.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    entry_formula.delete(0, END)
    entry_formula.insert(0, value+operation)

def calculate():
    value = entry_formula.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    entry_formula.delete(0, END)
    entry_formula.insert(0, eval(value))

def delete_all():
    entry_formula.delete(0,END)
   



app = CTk()
app.title('Calculator')
app.geometry('600x450')
app.resizable(False, False)

img = Image.open("img/send_plane.png")

entry_formula = CTkEntry(app, placeholder_text='0', width=15,
                         text_color='#a9a9a9', justify='right', font=('Arial', 22))
entry_formula.grid(row=0, column=0, columnspan=4, stick='we')

btn1 = CTkButton(app, text='1', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(1))
btn1.grid(row=1, column=0, stick='wens', padx=5, pady=5)

btn2 = CTkButton(app, text='2', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(2))
btn2.grid(row=1, column=1, stick='wens', padx=5, pady=5)

btn3 = CTkButton(app, text='3', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(3))
btn3.grid(row=1, column=2, stick='wens', padx=5, pady=5)

btn4 = CTkButton(app, text='4', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(4))
btn4.grid(row=2, column=0, stick='wens', padx=5, pady=5)

btn5 = CTkButton(app, text='5', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(5))
btn5.grid(row=2, column=1, stick='wens', padx=5, pady=5)

btn6 = CTkButton(app, text='6', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(6))
btn6.grid(row=2, column=2, stick='wens', padx=5, pady=5)

btn7 = CTkButton(app, text='7', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(7))
btn7.grid(row=3, column=0, stick='wens', padx=5, pady=5)

btn8 = CTkButton(app, text='8', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(8))
btn8.grid(row=3, column=1, stick='wens', padx=5, pady=5)

btn9 = CTkButton(app, text='9', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(9))
btn9.grid(row=3, column=2, stick='wens', padx=5, pady=5)

btn0 = CTkButton(app, text='0', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_digit(0))
btn0.grid(row=4, column=0, stick='wens', padx=5, pady=5)

btnplus = CTkButton(app, text='+', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_operation("+"))
btnplus.grid(row=4, column=2, stick='wens', padx=5, pady=5)

btnminus = CTkButton(app, text='-', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_operation("-"))
btnminus.grid(row=1, column=3, stick='wens', padx=5, pady=5)

btnumn = CTkButton(app, text='*', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_operation("*"))
btnumn.grid(row=2, column=3, stick='wens', padx=5, pady=5)

btndel = CTkButton(app, text='/', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=lambda: add_operation("/"))
btndel.grid(row=3, column=3, stick='wens', padx=5, pady=5)

btnrav = CTkButton(app, text='=', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=calculate)
btnrav.grid(row=4, column=3, stick='wens', padx=5, pady=5)

btnlast = CTkButton(app, text='C', fg_color='transparent', hover_color='#7b68ee',
                 border_color='#fafafa', border_width=1, command=delete_all)
btnlast.grid(row=4, column=1, stick='wens', padx=5, pady=5)

app.grid_columnconfigure(0, minsize=60)
app.grid_columnconfigure(1, minsize=60)
app.grid_columnconfigure(2, minsize=60)

app.grid_rowconfigure(1, minsize=60)
app.grid_rowconfigure(2, minsize=60)
app.grid_rowconfigure(3, minsize=60)
app.grid_rowconfigure(4, minsize=60)

# btn = CTkButton(app, text='Click me', corner_radius=30, fg_color='transparent', hover_color='#7b68ee',
# border_color='#fafafa', border_width=1, image=CTkImage(dark_image=img))
# btn.pack(anchor='c', pady=10)

app.mainloop()
