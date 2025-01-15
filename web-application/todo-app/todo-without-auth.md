# Flask TODO Application with User Authentication

## Introduction
This is a simple TODO application built with Flask, MySQL, and user authentication. Users can register, log in, and manage their tasks with a priority system.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

Python 3.x
MySQL Server
pip (Python package installer)
Installation
Clone the Repository
```
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
```
Create a Virtual Environment (Optional but recommended)

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
Install Required Packages
```
pip install Flask mysqlclient

```
## Database Setup
Log in to MySQL
```
mysql -u root -p

```
Create the Database and Tables Run the following SQL commands:

```

CREATE DATABASE py;

USE py;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## Configuration
Edit the Configuration in app.py Update the MySQL connection settings in app.py:

```
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'py'
```
## Running the Application
Start the Flask Application

```
python app.py

```
Access the Application Open your web browser and navigate to http://127.0.0.1:5000/.

## Usage


1. Add a New Task

    - Fill in the task title, description, and priority in the form on the main page and click "Add Task".
2. Edit an Existing Task

    - Click the "Edit" button next to a task to modify its details.
3. Delete a Task

    - Click the "Delete" button next to a task to remove it from the list.
4. View Tasks

    - All tasks will be displayed on the main page, sorted by priority.

