from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class DashboardWindow(QWidget):
    def __init__(self, username="Harsh"):
        super().__init__()

        self.setWindowTitle("Dashboard")

        # Set a modern font and window size
        self.setFont(QFont("JetBrains Mono", 12))
        self.setFixedSize(800, 600)

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

        # Create a grid layout for the dashboard
        layout = QGridLayout()

        # Adding labels and buttons
        self.label = QLabel(f"Welcome to the Dashboard, {username.capitalize()}!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("JetBrains Mono", 24, QFont.Bold))

        self.enter_marks_button = QPushButton("Enter Marks")
        self.enter_marks_button.clicked.connect(self.open_marks_feeding_window)
        
        self.view_marks_button = QPushButton("View Marks")
        self.view_marks_button.clicked.connect(self.open_marks_feeding_window)
        
        self.modify_marks_button = QPushButton("Edit Marks")
        self.modify_marks_button.clicked.connect(self.open_marks_feeding_window)
        
        self.reports_button = QPushButton("Generate Reports")
        self.reports_button.clicked.connect(self.open_coming_soon_window)
        
        self.attendance_button = QPushButton("Attendance Management")
        self.attendance_button.clicked.connect(self.open_coming_soon_window)
        
        self.export_button = QPushButton("Export Data")
        self.export_button.clicked.connect(self.open_coming_soon_window)
        

        # Add widgets to layout
        layout.addWidget(self.label, 0, 0, 1, 2)  # Spans across two columns
        layout.addWidget(self.enter_marks_button, 1, 0)
        layout.addWidget(self.view_marks_button, 1, 1)
        layout.addWidget(self.modify_marks_button, 2, 0)
        layout.addWidget(self.reports_button, 2, 1)
        layout.addWidget(self.attendance_button, 3, 0)
        layout.addWidget(self.export_button, 3, 1)

        self.setLayout(layout)

    def open_marks_feeding_window(self):
        from Dashboard.Marks_Sys.class_exam import ClassExamSelectionWindow
        
        self.class_exam_selection_window = ClassExamSelectionWindow()
        self.class_exam_selection_window.show()


    def open_coming_soon_window(self):
        from Dashboard.coming_soon import ComingSoonWindow
        self.coming_soon_window = ComingSoonWindow()
        self.coming_soon_window.show()

