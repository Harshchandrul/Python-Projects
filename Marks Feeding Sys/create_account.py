import customtkinter as ctk


def create_account_window():
    account_window = ctk.CTk()
    account_window.title("Create Account")

    # Username and password input fields
    label_username = ctk.CTkLabel(
        account_window, text="Username:", font=("JetBrains Mono", 16)
    )
    label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_username = ctk.CTkEntry(account_window, width=200)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    label_password = ctk.CTkLabel(
        account_window, text="Password:", font=("JetBrains Mono", 16)
    )
    label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_password = ctk.CTkEntry(account_window, show="*", width=200)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    # Subjects checkbox section
    label_subjects = ctk.CTkLabel(
        account_window, text="Select Subjects:", font=("JetBrains Mono", 16)
    )
    label_subjects.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    # Add multiple subject checkboxes
    subjects = {}
    subjects_list = [
        "Mathematics",
        "Science",
        "English",
        "Social Studies",
        "Computer Science",
        "Accounts",
        "Business Studies",
    ]
    for i, subject in enumerate(subjects_list):
        subjects[subject] = ctk.BooleanVar()  # Create a BooleanVar for each subject
        checkbox = ctk.CTkCheckBox(
            account_window, text=subject, variable=subjects[subject]
        )
        checkbox.grid(row=3 + i // 2, column=i % 2, padx=10, pady=5, sticky="w")

    # Create account button
    create_button = ctk.CTkButton(
        account_window,
        text="Create Account",
        command=lambda: save_account(
            entry_username.get(), entry_password.get(), subjects
        ),
    )
    create_button.grid(
        row=4 + len(subjects_list) // 2, column=0, columnspan=2, pady=20, padx=5
    )

    account_window.mainloop()


def save_account(username, password, subjects):
    # Extract selected subjects
    selected_subjects = [subject for subject, var in subjects.items() if var.get()]

    if not username or not password or not selected_subjects:
        print("Error: All fields must be filled and at least one subject selected!")
    else:
        # Save the account details logic (e.g., using dictionary, JSON, or database later)
        print(
            f"Account created for {username} with password {password} and subjects: {', '.join(selected_subjects)}"
        )
