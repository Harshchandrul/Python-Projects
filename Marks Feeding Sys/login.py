import customtkinter as ctk
from tkinter import messagebox
import json
import passkey

# Initailizing base custom theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
base_font = ("JetBrains Mono", 16)


# --------------------------------------------------------------------------
# ? LOGIN FUNCTIONALITY
# To load json file
def load_teachers():
    with open("teachers.json", "r") as file:
        return json.load(file)


# to check the login credentials
def check_login():
    username = entry_username.get()
    password = entry_password.get()

    teachers = load_teachers()  # Load data from JSON file
    if username in teachers and teachers[username]["password"] == password:
        messagebox.showinfo("Login Successful", f"Welcome {username}")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


# --------------------------------------------------------------------------
# ? TEXT BOX FOCUS FUNCTIONALITY
def on_focus_in(event, widget):
    widget.configure(border_color="light blue")


def on_focus_out(event, widget):
    widget.configure(border_color="gray")


# --------------------------------------------------------------------------
# ? WINDOW POSITION FUNCTIONALITY
def center_window(root, width, height):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x, y to center the window
    position_x = int((screen_width - width) / 2)
    position_y = int((screen_height - height) / 2)

    # Set the geometry of the window
    root.geometry(f"{width}x{height}+{position_x}+{position_y}")


# --------------------------------------------------------------------------
# ? ACCOUNT CREATION FUNCTIONALITY
def open_create_account():
    root.withdraw()  # Closing current window
    passkey.create_passkey_window()  # Opening passkey window


# --------------------------------------------------------------------------
# Login Window using CustomTkinter
root = ctk.CTk()
root.title("Login")

# Set window size (e.g., 400x300)
window_width = 400
window_height = 300
center_window(root, window_width, window_height)  # Call the center_window function

# --------------------------------------------------------------------------

# Username label and entry field
label_username = ctk.CTkLabel(root, text="Username:", font=base_font)
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_username = ctk.CTkEntry(root, width=200)
entry_username.grid(row=0, column=1, padx=10, pady=10)


# Password label and entry field
label_password = ctk.CTkLabel(root, text="Password:", font=base_font)
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_password = ctk.CTkEntry(root, show="*", width=200)
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Bind focus in and out events to change the border color
entry_username.bind("<FocusIn>", lambda event: on_focus_in(event, entry_username))
entry_username.bind("<FocusOut>", lambda event: on_focus_out(event, entry_username))

entry_password.bind("<FocusIn>", lambda event: on_focus_in(event, entry_password))
entry_password.bind("<FocusOut>", lambda event: on_focus_out(event, entry_password))

# Login button
login_button = ctk.CTkButton(root, text="Login", command=check_login, font=base_font)
login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=5)

# Creating Account link
create_account_label = ctk.CTkLabel(
    root, text="Create Account", font=("JetBrains Mono", 12, "underline")
)
create_account_label.grid(row=3, column=0, columnspan=2, pady=10, padx=5)
create_account_label.bind(
    "<Button-1>", lambda event: open_create_account()
)  # Adding link functionality

root.mainloop()
