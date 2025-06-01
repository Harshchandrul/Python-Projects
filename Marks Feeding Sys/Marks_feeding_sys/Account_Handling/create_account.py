from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QHBoxLayout,
    QMessageBox,
    QGridLayout,
    QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CreateAccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting window title and size
        self.setWindowTitle("Create Account Page")
        self.setFixedSize(800, 600)

        font = QFont("JetBrains Mono", 14)
        # Set a modern font and window size
        self.setFont(font)

        # Apply a modern stylesheet
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #433878;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #7E60BF;
            }
            QLabel {
                color: #FFE1FF;
            }
        """
        )

        # Creating Main layout
        layout = QGridLayout()

        # Creating Widgets
        self.name_label = QLabel("Name:")
        self.name_label.setFont(font)
        self.name_input = QLineEdit(self)
        self.name_input.setFont(font)

        self.password_label = QLabel("Password:")
        self.password_label.setFont(font)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.fav_dish_label = QLabel(
            "Favourite_Dish:"
        )
        self.fav_dish_label.setFont(font)
        self.fav_dish_input = QLineEdit(self)
        self.fav_dish_input.setFont(font)


        self.passkey_label = QLabel("Passkey (8 characters):")
        self.passkey_label.setFont(font)
        self.passkey_input = QLineEdit(self)
        self.passkey_input.setEchoMode(QLineEdit.Password)
        self.passkey_input.setMaxLength(8)  # Restrict to 8 characters

        # Subjects Label And checkboxes.
        self.subject_label = QLabel("Select Subject(s):")
        self.subject_label.setFont(font)
        scroll_area = QScrollArea()
        subjects_widget = QWidget()
        subjects_layout = QVBoxLayout(subjects_widget)

        # List of subjects with checkboxes
        self.subjects_list = [
            "Accounts",
            "Business Studies",
            "Economics",
            "English",
            "Computer",
            "Physics",
            "Chemistry",
            "Maths",
            "PHE",
            "Sanskrit",
            "Science",
            "SST",
        ]
        self.subject_checkboxes = []

        # Create checkboxes for each subject
        for subject in self.subjects_list:
            checkbox = QCheckBox(subject)
            checkbox.setFont(QFont("JetBrains Mono", 12))
            self.subject_checkboxes.append(checkbox)
            subjects_layout.addWidget(checkbox)

        # Set the scroll area widget and properties
        scroll_area.setWidget(subjects_widget)
        scroll_area.setWidgetResizable(True)
        

        # Create Account button
        self.create_button = QPushButton("Create Account")
        self.create_button.setFont(font)
        
        self.create_button.clicked.connect(self.create_account)

        # Adding widgets to layout
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.password_label, 1, 0)
        layout.addWidget(self.password_input, 1, 1)
        layout.addWidget(self.fav_dish_label, 2, 0)
        layout.addWidget(self.fav_dish_input, 2, 1)
        layout.addWidget(self.passkey_label, 3, 0)
        layout.addWidget(self.passkey_input, 3, 1)
        layout.addWidget(self.subject_label, 4, 0, 1, 2)

        layout.addWidget(scroll_area, 5, 0, 1, 2)  # Adding subject_layout to the main layout
        layout.addWidget(self.create_button, 6, 0, 1, 2)

        # Set central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_account(self):
        # Logic for creating the account
        name = self.name_input.text()
        password = self.password_input.text()
        fav_dish = self.fav_dish_input.text()
        passkey = self.passkey_input.text()
        selected_subjects = [
            checkbox.text()
            for checkbox in self.subject_checkboxes
            if checkbox.isChecked()
        ]

        # Check if all fields are filled and passkey is valid
        if (
            len(name) > 0
            and len(fav_dish) > 0
            and len(password) > 0
            and selected_subjects
        ):
            if passkey == "12345678":
                # Simulate account creation
                QMessageBox.information(
                    self,
                    "Account Created!",
                    f"Account created for {name} with subjects {selected_subjects}",
                )
                self.insert_teacher_data(name, password, selected_subjects, fav_dish)
            else:
                QMessageBox.warning(
                    self,
                    "Wrong Passkey",
                    "Please make sure passkey is 8 characters long and correct",
                )
        else:
            QMessageBox.warning(
                self,
                "Try Again!",
                "Please fill all fields and make sure passkey is exactly 8 characters.",
            )

    def insert_teacher_data(self, username, password, subjects, fav_dish):

        from db_connection import DatabaseConnection
        from mysql.connector import Error

        db = DatabaseConnection(database="teachers")
        connection = db.connect()

        if connection:

            try:
                cursor = connection.cursor()

                # %s acts as a placeholder for the values you want to insert.
                # When the query runs, Python will substitute each %s with the respective value from the tuple you pass.
                insert_query = """
                INSERT INTO TEACHERS (username, password, subjects, fav_dish)
                VALUES (%s, %s, %s, %s)
                """
                
                # Joining subjects list to make a string
                subjects_str = ", ".join(subjects)

                # Executing the query
                cursor.execute(
                    insert_query, (username, password, subjects_str, fav_dish)
                )

                # Commit the transaction to save the data in the database
                connection.commit()
                cursor.close()
                print("New teacher inserted successfully.")

            except Error as e:
                # For Handling any SQL or connection errors
                QMessageBox.warning(
                    None, "Error", f"Failed to create account: {str(e)}"
                )

            finally:
                db.close()
                self.close()
