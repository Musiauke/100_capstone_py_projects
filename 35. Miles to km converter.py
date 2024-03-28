from tkinter import *

def button_clicked():
    miles = float(input_entry.get())
    solution = miles * 1.609
    solution_label.config(text=f"{solution}")

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=40, pady=40)

my_label = Label(text='is equal to', font=('Arial', 24))
my_label.grid(column=0, row=2)
my_label.config(padx=0, pady=0)

miles_label = Label(text='Miles', font=('Arial', 24))
miles_label.grid(column=2, row=1)
miles_label.config(padx=0, pady=0)

km_label = Label(text='Km', font=('Arial', 24))
km_label.grid(column=2, row=2)
km_label.config(padx=0, pady=0)

solution_label = Label(text='', font=('Arial', 24))
solution_label.grid(column=1, row=2)
solution_label.config(padx=0, pady=0)

input_entry = Entry(width=10)
input_entry.grid(column=1, row=1)

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
