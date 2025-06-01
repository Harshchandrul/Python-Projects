from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from db_connection import DatabaseConnection  # Your custom database class


class MarksEntryWindow(QMainWindow):
    def __init__(self, class_selected, exam_selected, subjects_list):
        super().__init__()
        self.class_selected = class_selected
        self.exam_selected = exam_selected
        self.subjects_list = subjects_list
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Marks Entry Window")
        self.setFixedSize(800, 600)

        font = QFont(("JetBrains Mono", 16))
        self.setFont(font)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Title
        title = QLabel(f"Enter Marks for {self.class_selected} - {self.exam_selected}")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Table for marks entry
        self.marks_table = QTableWidget()
        self.marks_table.setColumnCount(len(self.subjects_list) + 2)  # Roll No, Name + Marks per subject
        self.marks_table.setHorizontalHeaderLabels(
            ["Roll No", "Name"] + [f"{sub}" for sub in self.subjects_list]
        )
        layout.addWidget(self.marks_table)

        # Save Button
        save_button = QPushButton("Save Marks")
        save_button.clicked.connect(self.save_marks)
        layout.addWidget(save_button)

        # Populate students and empty marks fields
        self.load_students()

    def load_students(self):
        """Load student data and their marks from the exam table and populate the table."""
        db = DatabaseConnection(database=self.class_selected)
        connection = db.connect()

        if connection:
            try:
                cursor = connection.cursor()

                # First, fetch the student roll numbers and names from the 'students' table
                cursor.execute(f"SELECT roll_no, name FROM students")
                students = cursor.fetchall()

                self.marks_table.setRowCount(len(students))

                # For each student, fetch the marks from the exam table
                for row, student in enumerate(students):
                    roll_no_item = QTableWidgetItem(str(student[0]))
                    name_item = QTableWidgetItem(student[1])

                    self.marks_table.setItem(row, 0, roll_no_item)  # Roll No
                    self.marks_table.setItem(row, 1, name_item)     # Name

                    # Now fetch the marks for this student from the exam table
                    cursor.execute(f"SELECT {', '.join([sub for sub in self.subjects_list])} "
                                f"FROM `{self.exam_selected}` WHERE roll_no = %s", (student[0],))
                    marks = cursor.fetchone()

                    # If there are existing marks, populate the table; otherwise, leave the fields empty
                    if marks:
                        for col, mark in enumerate(marks, start=2):  # Start from column 2 (skip Roll No, Name)
                            if mark is not None:  # Only set the value if a mark exists
                                self.marks_table.setItem(row, col, QTableWidgetItem(str(mark)))
                            else:
                                self.marks_table.setItem(row, col, QTableWidgetItem())  # Empty if no mark
                    else:
                        # If no marks are found, leave the fields empty
                        for col in range(2, len(self.subjects_list) + 2):
                            self.marks_table.setItem(row, col, QTableWidgetItem())

            finally:
                db.close()


    def save_marks(self):
        """Save the entered marks into the exam table, skipping empty fields."""
        
        db = DatabaseConnection(database=self.class_selected)
        connection = db.connect()

        if connection:
            try:
                cursor = connection.cursor()

                # Loop through each student (rows)
                for row in range(self.marks_table.rowCount()):
                    roll_no_item = self.marks_table.item(row, 0)  # Roll No
                    name_item = self.marks_table.item(row, 1)     # Student Name

                    # Check if roll number and name are available
                    if roll_no_item is None or name_item is None:
                        continue  # Skip this row if there's no roll number or name

                    roll_no = roll_no_item.text()
                    name = name_item.text()

                    # Prepare lists for columns and values to be inserted
                    insert_columns = ['roll_no', 'name']
                    insert_values = [roll_no, name]
                    
                    # Prepare lists for ON DUPLICATE KEY UPDATE
                    update_query_parts = []
                    update_values = []

                    # Loop through each subject (columns), skipping Roll No and Name columns
                    for col in range(2, self.marks_table.columnCount()):
                        subject_index = col - 2  # Adjust to subject index
                        subject_name = self.subjects_list[subject_index]

                        marks_obtained_item = self.marks_table.item(row, col)  # Marks Obtained

                        # If marks are entered (not empty), include them in the query
                        if marks_obtained_item is not None and marks_obtained_item.text():
                            marks_obtained = marks_obtained_item.text()
                            insert_columns.append(subject_name)
                            insert_values.append(marks_obtained)
                            update_query_parts.append(f"{subject_name} = %s")
                            update_values.append(marks_obtained)

                    # Only execute the query if there are any subjects with marks to save
                    if len(insert_columns) > 2:  # Means at least one subject has marks entered
                        insert_query = f"""
                            INSERT INTO `{self.exam_selected}` ({', '.join(insert_columns)})
                            VALUES ({', '.join(['%s'] * len(insert_columns))})
                            ON DUPLICATE KEY UPDATE {', '.join(update_query_parts)}
                        """
                        print("Executing query:", insert_query, insert_values + update_values)  # Debugging line
                        cursor.execute(insert_query, (*insert_values, *update_values))

                connection.commit()
                QMessageBox.information(self, "Success", "Marks saved successfully!")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error saving marks: {e}")
            
            finally:
                db.close()
