from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QSpinBox,
)
from PySide6.QtGui import QFont
from db_connection import DatabaseConnection


class StudentEntryWindow(QMainWindow):
    def __init__(self, class_selected):
        super().__init__()
        self.class_selected = class_selected

        self.setWindowTitle(f"Enter Students for {class_selected}")
        font = QFont("JetBrains Mono", 16)

        # Set a modern font and window size
        self.setFont(font)
        self.setFixedSize(500, 300)

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
        self.name_label = QLabel("Student Name:")
        self.name_label.setFont(font)
        self.name_input = QLineEdit()
        self.name_input.setFont(font)

        self.roll_label = QLabel("Roll Number:")
        self.roll_label.setFont(font)
        self.roll_input = QSpinBox()  # Use QSpinBox for roll number with arrow buttons
        self.roll_input.setMinimum(1)  # Set minimum roll number to 1 (or any starting value)
        self.roll_input.setMaximum(60)  # Maximum roll number (adjust as needed)
        self.roll_input.setFont(font)
        

        # Buttons
        self.add_button = QPushButton("Add Student")
        self.add_button.setFont(font)
        self.add_button.clicked.connect(self.add_student)

        self.finish_button = QPushButton("Finish")
        self.finish_button.setFont(font)
        self.finish_button.clicked.connect(self.finish_entry)

        # Add widgets to layout
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.roll_label, 1, 0)
        layout.addWidget(self.roll_input, 1, 1)
        layout.addWidget(self.add_button, 2, 0, 1, 2)
        layout.addWidget(self.finish_button, 3, 0, 1, 2)


    def add_student(self):
        student_name = self.name_input.text()
        roll_no = self.roll_input.text()

        if student_name and roll_no:
            db = DatabaseConnection(database=self.class_selected)
            connection = db.connect()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(
                        f"INSERT INTO students (name, roll_no) VALUES (%s, %s)",
                        (student_name, roll_no),
                    )

                    connection.commit()
                    cursor.close()

                    QMessageBox.information(
                        self,
                        "Success",
                        f"Student {student_name} with Roll_No {roll_no} added successfully!",
                    )
                    self.name_input.clear()

                finally:
                    db.close()
        else:
            QMessageBox.warning(
                self, "Error", "Please enter both name and roll number."
            )

    def finish_entry(self):
        class_selected = self.class_selected
        QMessageBox.information(
            self,
            "Thank You!",
            f"We've Got the required Data. Now you can feed marks of student for class {class_selected}",
        )
        self.close()
        
