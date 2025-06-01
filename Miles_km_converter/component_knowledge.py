from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
# To allow padding at the side of window
window.config(padx=10, pady=10)


def action():
    print("Do something")


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


def scale_used(value):
    print(value)


def radio_used():
    print(radio_state.get())


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)

# Buttons
# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=1)
new_button = Button(text="New Button", command=action)
new_button.grid(column=3, row=0)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=4, row=4)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))

# Spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)

# Scale
# Called with current scale value.
scale = Scale(from_=0, to=100, command=scale_used)

# Checkbutton
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()

# Radiobutton
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

# Listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
window.mainloop()


