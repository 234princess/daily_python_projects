from tkinter import *


def calculate():
    miles = entry.get()
    kilometer = round(float(miles) * 1.6)
    return solution.config(text=f'{kilometer}')


window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=250, height=125)
window.config(padx=20, pady=20)

entry = Entry(width=5)
entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals = Label(text="is equals to")
equals.grid(row=1, column=0)

solution = Label(text="0")
solution.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)


window.mainloop()

