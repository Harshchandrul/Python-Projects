# Login Functionality
from PySide6.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QLabel,
    QPushButton,
    QWidget,
    QMessageBox,
    QVBoxLayout,
    QGridLayout
)

from PySide6.QtCore import (
    Qt,
)  # It is imported to change the widget alignment, window states
from PySide6.QtGui import QFont  # It is imported to modify fonts in the window


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Form")
        self.setGeometry(470, 220, 500, 400)
        
        # Setting Custom Font
        self.setFont(QFont("JetBrains Mono", 14))

        # self.setStyleSheet(
        #     """
        #     QPushButton {
        #         background-color: #433878;
        #         color: white;
        #         padding: 10px;
        #         border-radius: 8px;
        #         font-size: 16px;
        #         margin: 5px;
        #     }
        #     QPushButton:hover {
        #         background-color: #7E60BF;
        #     }
        #     QLabel {
        #         color: #FFE1FF;
        #     }
        # """
        # )
        

        # Creating Layout
        layout = QGridLayout()

        # Creating Widgets -
        # Username label & field
        self.username_label = QLabel("Username:", self)
        

        self.username_input = QLineEdit(self)

        # Password Label $ field
        self.password_label = QLabel("Password:", self)

        self.password_input = QLineEdit(self)

        self.password_input.setEchoMode(QLineEdit.Password)  # To hide password input

        # Login Button
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.check_login)

        # self.login_button.setStyleSheet(
        #     """
        #     QPushButton {
        #         background-color: green;
        #         color: white;
        #         border-radius: 40px;
        #     }
        #     QPushButton:hover {
        #         background-color: darkgreen;
        #     }
        # """
        # )

        # Create Account Label
        self.create_account_label = QLabel(
            "<a href='#'>New Teacher? Create Account</a>", self
        )
        
        self.create_account_label.setFont(QFont("JetBrains Mono", 14))
        self.create_account_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_account_label.setStyleSheet("color: blue")
        self.create_account_label.linkActivated.connect(self.open_create_account_window)
        
        self.resert_password_label = QLabel(
            "<a href='#'>Forgot Password?</a>", self
        )

        self.resert_password_label.setFont(QFont("JetBrains Mono", 14))
        self.resert_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resert_password_label.setStyleSheet("color: blue")
        self.resert_password_label.linkActivated.connect(self.open_reset_password_window)


        # Adding widgets to layout
        layout.addWidget(self.username_label, 0, 0)
        layout.setSpacing(5)  # Reduce spacing between widgets
        layout.addWidget(self.username_input, 0, 1)
        layout.addWidget(self.password_label, 1, 0)
        layout.addWidget(self.password_input, 1, 1)
        layout.setSpacing(50)  # Adding extra space before button
        layout.addWidget(self.login_button, 2, 0, 1, 2)
        layout.addWidget(self.create_account_label, 3, 0, 1, 2)
        layout.addWidget(self.resert_password_label, 4, 0, 1, 2)

        # Setting Layout
        self.setLayout(layout)

        # Creating a central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Setting central widget of the window
        self.setCentralWidget(central_widget)

    def open_create_account_window(self):
        from Account_Handling.create_account import CreateAccountWindow
        self.create_account_window = CreateAccountWindow()
        self.create_account_window.show()    
        


    def check_login(self):
        # For accesing the text inside username and password input
        username = self.username_input.text()
        password = self.password_input.text()

        if self.authenticate_user(username, password):
            from Dashboard.dashboard import DashboardWindow 
            # self is passed here because it is the current instance of the login window (or whatever window you're working with). When you pass self, the message box is tied to this specific window and will appear in the context of that window.

            #  using self ensures that the warning message box is linked to the current login window, making it more intuitive for the user. Here's a visual example
            QMessageBox.information(self, "Login Success!", f"Welcome {username}")
            
            self.dashboard_window = DashboardWindow(username)
            self.dashboard_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed.", "Invalid username or password")


    def authenticate_user(self, username, password):
        try:
            from db_connection import DatabaseConnection
            db = DatabaseConnection(database="teachers")
            from mysql.connector import Error
            
            connection = db.connect()
            
            cursor = connection.cursor()
            authentication_query = """ SELECT password FROM teachers WHERE username = %s """
            cursor.execute(authentication_query, (username,))
            result = cursor.fetchone()

            # chechking if the usrname (row) even exists or not
            if result:
                stored_password = result[0]
                return password == stored_password  # Returns true if password matches
            else:
                return False
            
        except Error as e:
            QMessageBox.warning(self, "Error", f"Error Connecting To Database: {e}")
            return False
        
        finally:
            db.close()
            
            
    def open_reset_password_window(self):
        from Account_Handling.reset_password import ResetPasswordWindow
        self.reset_password_window = ResetPasswordWindow()
        self.reset_password_window.show()