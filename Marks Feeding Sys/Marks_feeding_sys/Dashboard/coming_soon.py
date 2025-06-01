from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class ComingSoonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advance Features")

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
        self.label = QLabel(f"COMING SOON!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("JetBrains Mono", 30, QFont.Bold))
        
        self.sub_label = QLabel(f"We are working hard to develop Soutions.\n Support us by funding Chandrul_Developers so that\n we can keep developing innovative and creative solutions\nfor your problems.🙂")
        self.sub_label.setAlignment(Qt.AlignCenter)
        self.sub_label.setFont(QFont("JetBrains Mono", 16))

        layout.addWidget(self.label, 0, 0, 1, 2)  # Spans across two columns
        layout.addWidget(self.sub_label, 1, 0)  # Spans across two columns

        
        self.setLayout(layout)