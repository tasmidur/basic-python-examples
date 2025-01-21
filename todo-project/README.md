# Django Installation and Project Structure

This document provides a step-by-step guide to installing Django and setting up a basic project structure.

---

## **1. Install Django**

### **Step 1: Install Python**

Django requires Python (version 3.6 or later). Download Python from the [official website](https://www.python.org/) and ensure it is added to your system's PATH.

To check if Python is installed, run:

```bash
python --version
```
or
```bash
python3 --version
```

---

### **Step 2: Create a Virtual Environment**

It's best practice to create a virtual environment to isolate your project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

---

### **Step 3: Install Django**

Install Django using pip:

```bash
pip3 install django
```

Verify the installation:

```bash
django-admin --version
```

---

## **2. Create a Django Project**

### **Step 1: Start a New Project**

Use the `django-admin startproject` command to create a new Django project:

```bash
django-admin startproject project_name
```

For example:

```bash
django-admin startproject todo
```

---

### **Step 2: Directory Structure**

After running the command, a directory named `todo` is created with the following structure:

```plaintext
todo/
    manage.py
    todo/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

- **Outer `todo/`**: The root directory for your project.
- **`manage.py`**: A command-line utility for managing the Django project. You can use it to start the development server, create migrations, etc.
- **Inner `todo/`**: Contains the project settings and configuration.

---

## **3. Explanation of Files**

### **Outer Directory: `todo/`**

- **`manage.py`**: A Python script to manage the project. Use it for commands like:
  - `python manage.py runserver` – Start the development server.
  - `python manage.py makemigrations` – Create migration files for database changes.
  - `python manage.py migrate` – Apply database migrations.

---

### **Inner Directory: `todo/`**

1. **`__init__.py`**:
   - Marks the directory as a Python package.

2. **`settings.py`**:
   - Contains the configuration for the project, such as database settings, installed apps, middleware, templates, and static files.

3. **`urls.py`**:
   - The URL configuration file. It maps URLs to their respective views.

4. **`asgi.py`**:
   - Entry point for ASGI (Asynchronous Server Gateway Interface) applications. Used for handling asynchronous web applications.

5. **`wsgi.py`**:
   - Entry point for WSGI (Web Server Gateway Interface) applications. Used for deploying the application.

---

## **4. Run the Development Server**

To verify the installation, navigate to the project directory and start the development server:

```bash
cd todo
python manage.py runserver
```

Open a web browser and go to `http://127.0.0.1:8000/`. You should see the Django welcome page.

---

## **5. Add an App to Your Project**

In Django, you organize features into apps. To create a new app, run:

```bash
python manage.py startapp app_name
```

For example:

```bash
python manage.py startapp blog
```

This creates a directory named `blog/` with the following structure:

```plaintext
blog/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

---

## **6. Project Structure with an App**

After creating an app, the project structure becomes:

```plaintext
todo/
    manage.py
    todo/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    blog/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```

- **`admin.py`**: Register models to manage them via the Django admin interface.
- **`apps.py`**: Application configuration.
- **`models.py`**: Define the database models.
- **`tests.py`**: Write test cases.
- **`views.py`**: Define the logic for rendering web pages.

---

## **7. Register the App**

To include the app in your project, add it to the `INSTALLED_APPS` list in `settings.py`:

```python
INSTALLED_APPS = [
    # Other installed apps
    'blog',
]
```

---

With this structure, you're ready to build and expand your Django project!

