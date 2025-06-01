import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="123456", database="teachers"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establishing the database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to the database established.")
                return self.connection
            
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def close(self):
        """Close the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
