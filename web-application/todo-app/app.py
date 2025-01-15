from flask import Flask, request, redirect, url_for, render_template
import MySQLdb

app = Flask(__name__)

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

@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY priority ASC")
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (title, description, priority) VALUES (%s, %s, %s)",
                   (title, description, priority))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
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
        cursor.execute("UPDATE tasks SET title = %s, description = %s, priority = %s WHERE id = %s",
                       (title, description, priority, task_id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('edit.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)