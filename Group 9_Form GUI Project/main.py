from tkinter import *
from NewForm import NewForm
import os

def new_form():
    new_form = NewForm()
    new_form.main()

def open_form():
    os.startfile('StudentDetails.xlsx')

window = Tk()
window.title('College Group Project Form')
logo_frame = Frame(window)
logo_frame.grid(row=0)
photo = PhotoImage(file="STCET.png")
clg_logo = Label(logo_frame, image=photo, width=500, height=500)
clg_logo.pack(side = TOP, anchor = CENTER)
button_frame = Frame(window)
button_frame.grid(row=1)
add = Button(button_frame, text='Add', bg='white', fg='black', width=10, padx=30, pady=10, command=new_form)
add.grid(row=1, column=0)
show = Button(button_frame, text='Show', bg='green', fg='white', width=10, padx=30, pady=10, command=open_form)
show.grid(row=1, column=1)
end = Button(button_frame, text='End', bg='red', fg='white', width=10, padx=30, pady=10, command=window.destroy)
end.grid(row=1, column=2)

window.mainloop()
