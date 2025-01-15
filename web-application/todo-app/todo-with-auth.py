from flask import Flask, request, redirect, url_for, render_template, session, flash
import MySQLdb
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'py'

def get_db_connection():
    return MySQLdb.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

# Middleware to check authentication
@app.before_request
def require_login():
    public_routes = ['login', 'register']
    if request.endpoint not in public_routes and 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        cursor.close()
        db.close()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user and check_password_hash(user[2], password):  # Assuming password is the 3rd column
            session['user_id'] = user[0]  # Assuming user ID is the 1st column
            session['username'] = user[1]  # Assuming username is the 2nd column
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/')
def index():
    user_id = session.get("user_id")  # Get the user ID from the session
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s ORDER BY priority ASC", (user_id,))
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', tasks=tasks,auth_user={
        'username': session.get('username'),
        'user_id': session.get('user_id')
    })

@app.route('/add', methods=['POST'])
def add_task():
    user_id = session.get("user_id")  # Get the user ID from the session
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    date = request.form['date']  # Ensure this is in the correct format (YYYY-MM-DD)

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (title, description, priority, user_id, date) VALUES (%s, %s, %s, %s, %s)",
                   (title, description, priority, user_id, date))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    db = get_db_connection()
    cursor = db.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        date = request.form['date']

        cursor.execute("UPDATE tasks SET title = %s, description = %s, priority = %s, date = %s WHERE id = %s",
                       (title, description, priority, date, task_id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)