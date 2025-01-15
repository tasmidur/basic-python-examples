# Python 3 Setup Guide

This guide provides step-by-step instructions to set up Python 3 on both Ubuntu and Windows.

---

## **Ubuntu**

### **Step 1: Update the Package Index**
```bash
sudo apt update && sudo apt upgrade -y
```

### **Step 2: Install Python 3**
```bash
sudo apt install python3 python3-pip -y
```

### **Step 3: Verify the Installation**
Check the installed Python and pip versions:
```bash
python3 --version
pip3 --version
```

### **Step 4: Install Virtual Environment (Optional)**
To manage Python dependencies, install the `venv` package:
```bash
sudo apt install python3-venv -y
```

Create a virtual environment:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

To deactivate the virtual environment:
```bash
deactivate
```

---

## **Windows**

### **Step 1: Download Python Installer**
1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Download the latest version for Windows.

### **Step 2: Run the Installer**
1. Launch the downloaded `.exe` file.
2. Check the **"Add Python to PATH"** box.
3. Click **Install Now**.

### **Step 3: Verify the Installation**
Open Command Prompt and check the installed versions:
```cmd
python --version
pip --version
```

### **Step 4: Install Virtual Environment (Optional)**
To manage dependencies, create a virtual environment:
```cmd
python -m venv myenv
myenv\Scripts\activate
```

To deactivate the virtual environment:
```cmd
deactivate
```

---

## **Common Commands**
- **Install a Package**:
  ```bash
  pip install package_name
  ```
- **Upgrade pip**:
  ```bash
  pip install --upgrade pip
  ```
- **List Installed Packages**:
  ```bash
  pip list
  ```

---

This guide should help you set up and get started with Python 3 on Ubuntu and Windows. Let me know if you need further assistance!

