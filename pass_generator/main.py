from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    password_generated = "".join(password_list)
    pass_entry.insert(END, password_generated)
    pass_entry.focus()
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entries():
    website = website_entry.get()
    email_s = email_entry.get()
    password_s = pass_entry.get()

    new_data = {
        website: {
            'email': email_s,
            'password': password_s
        }
    }

    if len(website) < 1 or len(password_s) < 1:
        messagebox.showwarning("Oops", "Dont leave any of the fields empty.")
        return
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Writing data into the file
                json.dump(data, data_file, indent=4)

        finally:
            # Clearing all the entries
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website_name = website_entry.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning("Oops!", "No Data File Found.\nFirst create one.")
    else:
        if website_name in data:
            messagebox.showinfo(f"Details of {website_name}",
                                f"\n Email: {data[website_name]['email']} \n Password: {data[website_name]['password']}")

        else:
            messagebox.showwarning("Oops", "No Website Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
window.minsize(400, 400)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
# canvas.grid(column=0, row=0)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_entry = Entry(width=31)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=50)
email_entry.insert(END, "harshchandrul@gmail.com")
email_entry.grid(column=1, columnspan=2, row=2)

pass_entry = Entry(width=31)
pass_entry.grid(column=1, row=3)

# Buttons
pass_gen_btn = Button(text="Generate Password", command=generate_password)
pass_gen_btn.grid(column=2, row=3)

search_btn = Button(text="Search", width=13, command=search_website)
search_btn.grid(column=2, row=1)

add_btn = Button(text="Add", width=41, command=add_entries)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
