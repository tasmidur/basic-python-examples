import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash
from config import Config

class UserModel:
    @staticmethod
    def get_connection():
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
    def create(name, email, password):
        connection = UserModel.get_connection()
        if connection is None:
            return None, "Database connection error"

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                return None, "User  Already Exists!"

            hashed_password = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users (name, email, password, created_at) VALUES (%s, %s, %s, NOW())",
                (name, email, hashed_password)
            )
            connection.commit()
            return {"Status": "Successfully Signed Up"}, None

        except Error as e:
            print(f"Error: {e}")
            return None, "Database error"

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = UserModel.get_connection()
        if connection is None:
            return None, "Database connection error"

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, name, email, created_at FROM users")
            records = cursor.fetchall()
            return records, None

        except Error as e:
            print(f"Error: {e}")
            return None, "Database error"

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(user_id, name):
        connection = UserModel.get_connection()
        if connection is None:
            return None, "Database connection error"

        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE users SET name = %s, updated_at = NOW() WHERE id = %s", (name, user_id))
            connection.commit()
            if cursor.rowcount == 0:
                return None, "User  not found"
            return {"Status": "Successfully Updated"}, None

        except Error as e:
            print(f"Error: {e}")
            return None, "Database error"

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(user_id):
        connection = UserModel.get_connection()
        if connection is None:
            return None, "Database connection error"

        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()
            if cursor.rowcount == 0:
                return None, "User  not found"
            return {"Status": "Successfully Deleted"}, None

        except Error as e:
            print(f"Error: {e}")
            return None, "Database error"

        finally:
            cursor.close()
            connection.close()