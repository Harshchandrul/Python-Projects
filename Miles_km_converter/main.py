# Miles to kilometer converter
from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(300, 300)
window.config(padx=20, pady=20)


def action():
    miles = miles_entry.get()
    km_text.config(text=int((int(miles) * 1.67)))


label = Label(text="Is equal to:")
label.grid(column=0, row=1)

miles_entry = Entry(width=10)
# miles_entry.insert(END, "0")
miles_entry.grid(column=1, row=0)

km_text = Label(text="0")
km_text.grid(column=1, row=1)

label_2 = Label(text="miles")
label_2.grid(column=2, row=0)
label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

# Calculate button
button = Button(text="calculate", command=action)
button.grid(column=1, row=2)


window.mainloop()





