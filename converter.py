from tkinter import *
FONT = ("Courier", 14)


def reset():
    from_label.config(text="° F")
    to_label.config(text="° C")
    listbox.selection_clear(first=0, last=7)
    entry.delete(first=0, last=7)
    value.config(text="0")


def f_to_c():
    from_label.config(text="° F")
    to_label.config(text="° C")
    calculation = round((int(entry.get()) - 32) * 5/9, 1)
    value.config(text=calculation)


def miles_to_km():
    from_label.config(text="miles")
    to_label.config(text="km ")
    calculation = round(int(entry.get()) * 1.609, 1)
    value.config(text=calculation)


def gal_to_l():
    from_label.config(text="gallons")
    to_label.config(text="liters ")
    calculation = round(int(entry.get()) * 3.78541, 1)
    value.config(text=calculation)


def listbox_used(event):
    if entry.get() != "":
        conversion = conversions_dict[listbox.get(listbox.curselection())]
        conversion()


conversions_dict = {
    "° F to ° C": f_to_c,
    "miles to km": miles_to_km,
    "gallons to l": gal_to_l,
}


window = Tk()
window.title("Converter")
window.config(padx=50, pady=50)

# Elements
entry = Entry(width=5, font=FONT)
entry.focus()
entry.grid(row=0, column=1)

from_label = Label(text="° F", font=FONT)
from_label.grid(row=0, column=2)

eq_label = Label(text="is equal to", font=FONT)
eq_label.grid(row=1, column=0)

value = Label(text=0, font=FONT)
value.grid(row=1, column=1)

to_label = Label(text="° C", font=FONT)
to_label.grid(row=1,column=2)

listbox = Listbox(height=3, exportselection=False)
conversions = ['° F to ° C', 'miles to km', 'gallons to l']
for item in conversions:
    listbox.insert(conversions.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=2, column=0)

button = Button(text="Reset", command=reset, font=FONT)
button.grid(row=2, column=1)


window.mainloop()
