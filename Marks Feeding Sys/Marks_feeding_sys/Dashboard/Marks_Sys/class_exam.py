# First Here we will make Class and Exam selection Window

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton,
    QMessageBox,
    QGridLayout,
    QCheckBox,
    QVBoxLayout,
    QScrollArea,
)

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont

from db_connection import DatabaseConnection  # Your custom database class


class ClassExamSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Class and Exam")

        # Set a modern font and window size
        self.setFont(QFont("JetBrains Mono", 16))
        self.setFixedSize(800, 600)

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

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
            QComboBox {
                color: #FFE1FF
            }
        """
        )

        # Layout
        layout = QGridLayout(central_widget)

        # Class Selection
        self.class_label = QLabel("Select Class:")
        self.class_label.setFont(QFont("JetBrains Mono", 16))
        self.class_combo = QComboBox()
        self.class_combo.addItems(
            [
                "12_A",
                "12_B",
                "11_A",
                "11_B",
                "10_A",
                "10_B",
                "10_C",
                "9_A",
                "9_B",
                "9_C",
                "8_A",
                "8_B",
                "8_C",
                "7_A",
                "7_B",
                "7_C",
                "6_A",
                "6_B",
                "6_C",
                "5_A",
                "5_B",
                "5_C",
            ]
        )  # Add class options

        # Exam Selection
        self.exam_label = QLabel("Select Exam:")
        self.exam_label.setFont(QFont("JetBrains Mono", 16))
        self.exam_combo = QComboBox()
        self.exam_combo.addItems(["Half_Yearly", "Final_Exam"])  # Add exam options
        self.exam_combo.setFont(QFont("JetBrains Mono", 16))
        
        # Create a label to notify about pre-selected subjects
        self.subjects_skip_label = QLabel("Subjects already selected, no need to choose again.")
        self.subjects_skip_label.setFont(QFont("JetBrains Mono", 16))
        self.subjects_skip_label.hide()  # Initially hidden

        # Here i will put checkboxes to check how many subjects each class have
        # Subject Selection
        self.subject_label = QLabel("Select Subjects The Class Offers:")
        self.subject_label.setFont(QFont("JetBrains Mono", 16))

        # Create a scrollable area for subjects (in case of a large number of subjects)
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
            checkbox.setFont(QFont("JetBrains Mono", 14))
            self.subject_checkboxes.append(checkbox)
            subjects_layout.addWidget(checkbox)

        # Set the scroll area widget and properties
        scroll_area.setWidget(subjects_widget)
        scroll_area.setWidgetResizable(True)

        # Proceed Button
        self.proceed_button = QPushButton("Proceed")
        self.proceed_button.clicked.connect(self.check_class_and_exam)

        # Adding widgets to the grid layout
        layout.addWidget(self.class_label, 0, 0)
        layout.addWidget(self.class_combo, 0, 1)
        layout.addWidget(self.exam_label, 1, 0)
        layout.addWidget(self.exam_combo, 1, 1)
        layout.addWidget(self.subjects_skip_label, 2, 0, 1, 2)
        layout.addWidget(self.subject_label, 3, 0, 1, 2)
        layout.addWidget(scroll_area, 4, 0, 1, 2)  # Add scroll area for subjects
        layout.addWidget(self.proceed_button, 5, 0, 1, 2)

    # Inside ClassExamSelectionWindow
    
    def exam_table_exists(self):
        return True
    

    def create_database(self, class_selected):
        db = DatabaseConnection(database=None)  # Connect without a specific database
        connection = db.connect()
        if connection:
            try:
                cursor = connection.cursor()

                # Create the database if it doesn't exist
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{class_selected}`")
                cursor.execute(f"USE {class_selected}")
                cursor.close()
                print(f"Database `{class_selected}` created or already exists.")

            finally:
                db.close()
                

    # Function to create tables if they don't exist
    def create_table(self, class_selected, exam_selected):
        db = DatabaseConnection(
            database=class_selected
        )  # Use the class-specific database
        connection = db.connect()
        if connection:
            try:
                cursor = connection.cursor()

                # Use the selected class database
                cursor.execute(f"USE `{class_selected}`")

                # Build the table structure with 'name' and 'roll_no' fields
                columns = [
                    "roll_no INT PRIMARY KEY",
                    "name VARCHAR(100) NOT NULL",
                ]
                
                self.checked_subjects = []

                # Add a column for each selected subject
                for checkbox in self.subject_checkboxes:
                    if checkbox.isChecked():
                        subject = (
                            checkbox.text().replace(" ", "_").lower()
                        )  # Convert subject names to valid SQL format
                        self.checked_subjects.append(subject)
                        columns.append(
                            f"{subject} INT"
                        )  # Create an INT field for each subject to store marks

                # Construct the SQL query to create the exam table
                exam_table_query = f"""
                CREATE TABLE IF NOT EXISTS `{exam_selected}` (
                    {', '.join(columns)}
                );
                """

                # Execute the query to create the table
                cursor.execute(exam_table_query)

                # Commit the changes and close the cursor
                connection.commit()
                cursor.close()
                print(
                    f"Table `{exam_selected}` created successfully in `{class_selected}`."
                )

            finally:
                db.close()

    def check_class_and_exam(self):
        class_selected = self.class_combo.currentText()
        exam_selected = self.exam_combo.currentText()
        # Create a database connection
        db = DatabaseConnection(database=None)
        connection = db.connect()

        if connection:
            cursor = connection.cursor()

            # Check if the class database exists
            cursor.execute(f"SHOW DATABASES LIKE '{class_selected}'")
            class_exists = cursor.fetchone()

            if not class_exists:
                self.create_database(class_selected)
                

            # Use the class database
            cursor.execute(f"USE {class_selected}")
            
            # Check if the exam table exists in the class database
            cursor.execute(f"SHOW TABLES LIKE '{exam_selected}'")
            exam_table_exists = cursor.fetchone()

            if not exam_table_exists:
                # Create the exam table if it doesn't exist
                self.create_table(class_selected, exam_selected)
                print(f"Table {exam_selected} created in database {class_selected}.")
            else:
                print(
                    f"Table {exam_selected} already exists in database {class_selected}."
                )

            # Commit the changes and close the connection
            cursor.fetchall()
            connection.commit()

            # Check if the student table exists
            cursor.execute(f"SHOW TABLES LIKE 'students'")
            student_table_exists = cursor.fetchone()

            if student_table_exists:
                # Open marks entry window
                self.checked_subjects = []
                # Add a column for each selected subject
                for checkbox in self.subject_checkboxes:
                    if checkbox.isChecked():
                        subject = (
                            checkbox.text().replace(" ", "_").lower()
                        )  # Convert subject names to valid SQL format
                        self.checked_subjects.append(subject)
                        
                self.open_marks_entry_window(class_selected, exam_selected, self.checked_subjects)

            else:
                create_students_table = """
                CREATE TABLE IF NOT EXISTS STUDENTS 
                (roll_no INT PRIMARY KEY NOT NULL, name VARCHAR(50) NOT NULL)
                """
                cursor.execute(create_students_table)
                # Open student entry window
                self.open_student_entry_window(class_selected)

            cursor.close()
            db.close()

            # Move to the next step (e.g., opening the marks entry window)
        else:
            QMessageBox.critical(self, "Error", "Failed to connect to the database.")

    def open_student_entry_window(self, class_selected):
        from Dashboard.Marks_Sys.students_entry import StudentEntryWindow
        self.student_entry_window = StudentEntryWindow(class_selected)
        self.student_entry_window.show()

    def open_marks_entry_window(self, class_selected, exam_selected, subject_list):
        from Dashboard.Marks_Sys.marks_entry import MarksEntryWindow
        self.marks_entry_window = MarksEntryWindow(class_selected, exam_selected, subject_list)
        self.marks_entry_window.show()
        
