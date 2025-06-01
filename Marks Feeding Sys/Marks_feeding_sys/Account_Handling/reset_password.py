from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QMessageBox,
)
from PySide6.QtGui import QFont
from db_connection import DatabaseConnection
from Account_Handling.login import LoginWindow


class ResetPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reset Password")
        font = QFont("JetBrains Mono", 14)

        # Set a modern font and window size
        self.setFont(font)
        self.setFixedSize(600, 400)

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

        # Set up the layout and UI elements
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Input fields
        self.username = QLabel("Username:")
        self.username.setFont(font)
        self.username_input = QLineEdit()
        self.username_input.setFont(font)

        self.new_pass = QLabel("New Password:")
        self.new_pass.setFont(font)
        self.new_pass_input = QLineEdit()
        self.new_pass_input.setFont(font)
        self.new_pass_input.setEchoMode(QLineEdit.Password)

        self.confirm_new_pass = QLabel("Confirm Password:")
        self.confirm_new_pass.setFont(font)
        self.confirm_new_pass_input = QLineEdit()
        self.confirm_new_pass_input.setFont(font)
        self.confirm_new_pass_input.setEchoMode(QLineEdit.Password)

        self.fav_dish = QLabel("Favourite Dish:")
        self.fav_dish.setFont(font)
        self.fav_dish_input = QLineEdit()
        self.fav_dish_input.setFont(font)

        self.finish_button = QPushButton("Reset Password")
        self.finish_button.setFont(font)
        self.finish_button.clicked.connect(self.reset_password)

        layout.addWidget(self.username, 0, 0)
        layout.addWidget(self.username_input, 0, 1)
        layout.addWidget(self.new_pass, 1, 0)
        layout.addWidget(self.new_pass_input, 1, 1)
        layout.addWidget(self.confirm_new_pass, 2, 0)
        layout.addWidget(self.confirm_new_pass_input, 2, 1)
        layout.addWidget(self.fav_dish, 4, 0)
        layout.addWidget(self.fav_dish_input, 4, 1)
        layout.addWidget(self.finish_button, 5, 0, 1, 2)

    def reset_password(self):
        db = DatabaseConnection(database="teachers")
        connection = db.connect()
        username = self.username_input.text()
        new_password = self.new_pass_input.text()
        confirm_password = self.confirm_new_pass_input.text()
        fav_dish_input = self.fav_dish_input.text()

        if (
            not username
            or not new_password
            or not confirm_password
            or not fav_dish_input
        ):
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        if connection:
            try:
                cursor = connection.cursor()
                authentication_query = (
                    "SELECT fav_dish FROM teachers WHERE username = %s"
                )
                cursor.execute(authentication_query, (username,))
                result = cursor.fetchone()

                if result and result[0] == fav_dish_input:
                    # User authenticated, update the password
                    update_query = (
                        "UPDATE teachers SET password = %s WHERE username = %s"
                    )
                    cursor.execute(update_query, (new_password, username))
                    connection.commit()
                    QMessageBox.information(
                        self, "Success", "Password reset successfully!"
                    )
                    self.close()
                else:
                    QMessageBox.warning(
                        self, "Error", "Incorrect username or favourite dish."
                    )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error occurred: {e}")
            finally:
                db.close()
        else:
            QMessageBox.critical(self, "Error", "Database connection failed.")
