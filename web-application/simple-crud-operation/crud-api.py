from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

# Create a MySQL connection
def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def base():
    return {'Status': 'UP'}

# Create (Insert Record)
@app.route('/signup', methods=['POST'])
def insert_record():
    data = request.json

    # Validate input
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"Status": "Invalid input"}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({"Status": "Database connection error"}), 500

    cursor = connection.cursor()

    try:
        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (data['email'],))
        if cursor.fetchone():
            return jsonify({"Status": "User  Already Exists!"}), 400

        # Hash the password
        hashed_password = generate_password_hash(data['password'])

        # Insert new user with timestamp
        cursor.execute(
            "INSERT INTO users (name, email, password, created_at) VALUES (%s, %s, %s, NOW())",
            (data['name'], data['email'], hashed_password)
        )
        connection.commit()
        return jsonify({"Status": "Successfully Signed Up"}), 201

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Status": "Database error"}), 500

    finally:
        cursor.close()
        connection.close()

# Read (Get Records)
@app.route('/read', methods=['GET'])
def read_record():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"Status": "Database connection error"}), 500

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT id, name, email, created_at FROM users")  # Exclude password
        records = cursor.fetchall()
        return jsonify(records), 200

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Status": "Database error"}), 500

    finally:
        cursor.close()
        connection.close()

# Update (Modify Record)
@app.route('/update/<int:user_id>', methods=['PUT'])
def update_record(user_id):
    data = request.json

    # Validate input
    if not data or 'name' not in data:
        return jsonify({"Status": "Invalid input"}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({"Status": "Database connection error"}), 500

    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE users SET name = %s, updated_at = NOW() WHERE id = %s", (data['name'], user_id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"Status": "User  not found"}), 404
        return jsonify({"Status": "Successfully Updated"}), 200

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Status": "Database error"}), 500

    finally:
        cursor.close()
        connection.close()


# Delete (Remove Record)
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_record(user_id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({"Status": "Database connection error"}), 500

    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"Status": "User  not found"}), 404
        return jsonify({"Status": "Successfully Deleted"}), 200

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Status": "Database error"}), 500

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(port=5000, debug=True)  # Run the app on port 5000