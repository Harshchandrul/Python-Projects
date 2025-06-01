# Rendering the application
from PySide6.QtWidgets import QApplication
import sys
from Account_Handling.login import LoginWindow
from db_connection import DatabaseConnection

# Function to create a database if it doesn't exist
def create_database():
    db = DatabaseConnection(database="teachers")
    connection = db.connect()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS teachers")
            cursor.execute("USE teachers")
            cursor.close()
        finally:
            db.close()


# Function to create tables if they don't exist
def create_tables():
    db = DatabaseConnection(database="teachers")
    connection = db.connect()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("USE teachers")  # Switch to your database

            # Create teachers table
            teachers_table = """
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                subjects VARCHAR(255) NOT NULL,
                fav_dish VARCHAR(100) NOT NULL
            );
            """
            cursor.execute(teachers_table)

            connection.commit()
            cursor.close()

        finally:
            db.close()


# Function to initialize the database and tables
def initialize_database():
    create_database()
    create_tables()


# Main function to run the application
if __name__ == "__main__":
    initialize_database()
    app = QApplication(sys.argv)
    # window = LoginWindow()
    # window.show()
    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
