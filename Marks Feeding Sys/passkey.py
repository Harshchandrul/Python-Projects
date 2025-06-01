import customtkinter as ctk
import create_account
from tkinter import messagebox


def create_passkey_window():
    passkey_window = ctk.CTk()
    passkey_window.title("Enter Passkey")

    def verify_passkey():
        entered_key = passkey_entry.get()
        if entered_key == "123":  # Replace with your actual passkey
            passkey_window.destroy()  # Close passkey window
            create_account.create_account_window()  # Open account creation window
        else:
            messagebox.showerror("Error", "Invalid passkey")

    # Create passkey entry
    label_passkey = ctk.CTkLabel(
        passkey_window, text="Enter Passkey:", font=("JetBrains Mono", 16)
    )
    label_passkey.pack(pady=10)
    passkey_entry = ctk.CTkEntry(passkey_window, show="*", width=200)
    passkey_entry.pack(pady=10)

    # Submit button
    submit_button = ctk.CTkButton(passkey_window, text="Submit", command=verify_passkey)
    submit_button.pack(pady=20)

    passkey_window.mainloop()
