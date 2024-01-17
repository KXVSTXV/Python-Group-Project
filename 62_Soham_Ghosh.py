from tkinter import *
import math

global degrad

def button_pressed(button):
    display.insert(END, button)

def clearall():
    display.delete(0, END)

def clear_preceding():
    expression = display.get()
    display.delete(len(expression)-1, END)

def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, END)
        display.insert(0, result)
    except ZeroDivisionError:
        display.delete(0, END)
        display.insert(0, "Undefined")

def square_root():
    try:
        result = str(math.sqrt(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def sin():
    try:
        result = str(math.sin(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def arcsin():
    try:
        result = str(math.asin(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def cos():
    try:
        result = str(math.cos(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def arccos():
    try:
        result = str(math.acos(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def tan():
    try:
        result = str(math.tan(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def arctan():
    try:
        result = str(math.atan(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def log():
    try:
        result = str(math.log10(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def ln():
    try:
        result = str(math.log2(float(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def degrad():
    degrad = 'Radian'
    if degrad == 'Radian':
        try:
            result = str(math.degrees(float(display.get())))
            print(result)
            print(type(result))
            display.delete(0, END)
            display.insert(0, result)
            degrad = 'Degree'
            degree_radian.config(text='Rad')
        except:
            display.delete(0, END)
            display.insert(0, "ERROR")
    elif degrad == 'Degree':
        try:
            result = str(math.radians(float(display.get())))
            display.delete(0, END)
            display.insert(0, result)
            degrad = 'Radian'
            degree_radian.config(text='Deg')
        except:
            display.delete(0, END)
            display.insert(0, "ERROR")

def fact():
    try:
        result = str(math.factorial(int(display.get())))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def plus_minus():
    try:
        current = display.get()
        if current != '' and current[0] == '-':
            display.delete(0)
        else:
            display.insert(0, '-')
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

window = Tk()
window.title('Calculator')
window.configure(background='#D3D3D3')
calc_frame = Frame(window).grid()

display = Entry(calc_frame, bg='white', fg='black', width=90)
display.grid(columnspan=6)

sqrt = Button(calc_frame, text='SQRT', width=10, bg='gray', fg='black', command=square_root).grid(row=2, column=0, padx = 5, pady = 5)
power = Button(calc_frame, text='POW', width=10, bg='gray', fg='black', command=lambda:button_pressed('**')).grid(row=2, column=1, padx = 5, pady = 5)
degree_radian = Button(calc_frame, text='Deg', width=10, bg='gray', fg='black', command=degrad)
degree_radian.grid(row=2, column=2, padx = 5, pady = 5)
clear2 = Button(calc_frame, text='CE', width=10, bg='gray', fg='black', command=clear_preceding).grid(row=2, column=3, padx = 5, pady = 5)
clear = Button(calc_frame, text='AC', width=10, bg='gray', fg='black', command=clearall).grid(row=2, column=4, padx = 5, pady = 5)
end = Button(calc_frame, text='End', width=10, bg='gray', fg='black', command=window.destroy).grid(row=2, column=5, padx = 5, pady = 5)
button7 = Button(calc_frame, text='7', width=10, bg='light gray', fg='black', command=lambda:button_pressed('7')).grid(row=3, column=0, padx = 5, pady = 5)
button8 = Button(calc_frame, text='8', width=10, bg='light gray', fg='black', command=lambda:button_pressed('8')).grid(row=3, column=1, padx = 5, pady = 5)
button9 = Button(calc_frame, text='9', width=10, bg='light gray', fg='black', command=lambda:button_pressed('9')).grid(row=3, column=2, padx = 5, pady = 5)
add = Button(calc_frame, text='+', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('+')).grid(row=3, column=3, padx = 5, pady = 5)
sin = Button(calc_frame, text='sin', width=10, bg='gray', fg='black', command=sin).grid(row=3, column=4, padx = 5, pady = 5)
arcsin = Button(calc_frame, text='sin^-1', width=10, bg='gray', fg='black', command=arcsin).grid(row=3, column=5, padx = 5, pady = 5)
button4 = Button(calc_frame, text='4', width=10, bg='light gray', fg='black', command=lambda:button_pressed('4')).grid(row=4, column=0, padx = 5, pady = 5)
button5 = Button(calc_frame, text='5', width=10, bg='light gray', fg='black', command=lambda:button_pressed('5')).grid(row=4, column=1, padx = 5, pady = 5)
button6 = Button(calc_frame, text='6', width=10, bg='light gray', fg='black', command=lambda:button_pressed('6')).grid(row=4, column=2, padx = 5, pady = 5)
subtract = Button(calc_frame, text='-', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('-')).grid(row=4, column=3, padx = 5, pady = 5)
cos = Button(calc_frame, text='cos', width=10, bg='gray', fg='black', command=cos).grid(row=4, column=4, padx = 5, pady = 5)
arccos = Button(calc_frame, text='cos^-1', width=10, bg='gray', fg='black', command=arccos).grid(row=4, column=5, padx = 5, pady = 5)
button1 = Button(calc_frame, text='1', width=10, bg='light gray', fg='black', command=lambda:button_pressed('1')).grid(row=5, column=0, padx = 5, pady = 5)
button2 = Button(calc_frame, text='2', width=10, bg='light gray', fg='black', command=lambda:button_pressed('2')).grid(row=5, column=1, padx = 5, pady = 5)
button3 = Button(calc_frame, text='3', width=10, bg='light gray', fg='black', command=lambda:button_pressed('3')).grid(row=5, column=2, padx = 5, pady = 5)
multiply = Button(calc_frame, text='*', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('*')).grid(row=5, column=3, padx = 5, pady = 5)
tan = Button(calc_frame, text='tan', width=10, bg='gray', fg='black', command=tan).grid(row=5, column=4, padx = 5, pady = 5)
arctan = Button(calc_frame, text='tan^-1', width=10, bg='gray', fg='black', command=arctan).grid(row=5, column=5, padx = 5, pady = 5)
button0 = Button(calc_frame, text='0', width=10, bg='light gray', fg='black', command=lambda:button_pressed('0')).grid(row=6, column=0, padx = 5, pady = 5)
decimal_pt = Button(calc_frame, text='.', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('.')).grid(row=6, column=1, padx = 5, pady = 5)
plus_minus = Button(calc_frame, text='±', width=10, bg='dark gray', fg='black', command=plus_minus).grid(row=6, column=2, padx = 5, pady = 5)
divide = Button(calc_frame, text='/', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('/')).grid(row=6, column=3, padx = 5, pady = 5)
log = Button(calc_frame, text='log', width=10, bg='gray', fg='black', command=log).grid(row=6, column=4, padx = 5, pady = 5)
fact = Button(calc_frame, text='x!', width=10, bg='gray', fg='black', command=fact).grid(row=6, column=5, padx = 5, pady = 5)
bracket_open = Button(calc_frame, text='(', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('(')).grid(row=7, column=0, padx = 5, pady = 5)
bracket_open = Button(calc_frame, text=')', width=10, bg='dark gray', fg='black', command=lambda:button_pressed(')')).grid(row=7, column=1, padx = 5, pady = 5)
equals = Button(calc_frame, text='=', width=10, bg='dark gray', fg='black', command=calculate).grid(row=7, column=2, padx = 5, pady = 5)
modulus = Button(calc_frame, text='%', width=10, bg='dark gray', fg='black', command=lambda:button_pressed('%')).grid(row=7, column=3, padx = 5, pady = 5)
ln = Button(calc_frame, text='ln', width=10, bg='gray', fg='black', command=ln).grid(row=7, column=4, padx = 5, pady = 5)
pi = Button(calc_frame, text='π', width=10, bg='gray', fg='black', command=lambda:button_pressed('*'+str(math.pi))).grid(row=7, column=5, padx = 5, pady = 5)
window.mainloop()
