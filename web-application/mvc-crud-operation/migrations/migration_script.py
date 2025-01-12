import mysql.connector
from mysql.connector import Error
from config import Config
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Migration:
    @staticmethod
    def get_connection():
        """Establish a database connection."""
        try:
            return mysql.connector.connect(
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                host=Config.DB_HOST,
                database=Config.DB_NAME
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    @staticmethod
    def create_users_table():
        """Create the users table."""
        connection = Migration.get_connection()
        if connection is None:
            return "Database connection error"

        create_table_query = """
        CREATE TABLE IF NOT EXISTS user2 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        """

        cursor = connection.cursor()
        try:
            cursor.execute(create_table_query)
            connection.commit()
            print("Users table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def drop_users_table():
        """Drop the users table."""
        connection = Migration.get_connection()
        if connection is None:
            return "Database connection error"

        drop_table_query = "DROP TABLE IF EXISTS user2;"

        cursor = connection.cursor()
        try:
            cursor.execute(drop_table_query)
            connection.commit()
            print("Users table dropped successfully.")
        except Error as e:
            print(f"Error dropping table: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Run the migration to create the users table
    # for execute `python migrations/migration_script.py`
    Migration.create_users_table()