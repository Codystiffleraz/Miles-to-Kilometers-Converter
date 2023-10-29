from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)

# create the window 
# create the entry widget
# create a button
# create the surrounding text
# create where the output should be 

buffer = Label(text="",width=8)
buffer.grid(column=0, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

answer = Label(text="")
answer.grid(column=1, row=1)\

km = Label(text="Km")
km.grid(column=2,row=1)

def button_clicked():
    number = float(input.get())
    formula = round(number * 1.609344,2)
    answer.config(text=formula)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()