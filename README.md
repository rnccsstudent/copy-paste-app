# 📋 Fast Copy Paste App

A minimalistic, fast, and simple web app to copy, save, view, download, and delete text using a Flask backend and a lightweight HTML frontend.

---

## 🔗 Live URL

**Frontend**: Deployed on Netlify  
**Backend**: Deployed on PythonAnywhere  
**API Base URL**: `https://pranabmahata.pythonanywhere.com`

---

## 🖼️ Features

- Paste or write text in the input box
- 📋 Copy & save text to the server (and clipboard)
- 👁️ View previously saved text
- ⬇️ Download saved text as a `.txt` file
- 🗑️ Delete saved text

---

## 🧠 Technology Stack

| Layer     | Technology |
|-----------|------------|
| Frontend  | HTML, JavaScript, Bootstrap |
| Backend   | Python, Flask |
| Hosting   | Netlify (Frontend), PythonAnywhere (Backend) |

---
### 🚀 Deploying Instructions
    🔹 PythonAnywhere (Backend)
    Create a Python 3.10+ web app.

    Upload app.py and requirements.txt.

Set up a virtualenv with:

    pip install -r requirements.txt
    Point WSGI file to app.py

Reload the web app

---

### 🔹 Netlify (Frontend)

Create a new site from your index.html

Make sure API URLs match https://your-pythonanywhere-username.pythonanywhere.com

---

### 📜 License

This project is open-source and free to use for any purpose.

---

### Virtual Environment Guide

Step 1: Create a virtualenv (if you haven't already)
Open a Bash console on PythonAnywhere.

Run this command to create a Python 3.10 virtualenv named myvenv (you can choose a different name if you want):

    python3.10 -m venv ~/myvenv
This creates a folder myvenv inside your home directory with a separate Python environment.

Step 2: Activate the virtualenv and install required packages
Run:

    source ~/myvenv/bin/activate
    pip install --upgrade pip
    pip install flask flask-cors
This installs Flask and Flask-CORS inside your virtualenv.

Step 3: Configure PythonAnywhere to use the virtualenv

Go to the Web tab on PythonAnywhere.

Find the section Virtualenv (where it says Enter path to a virtualenv, if desired).

Enter the path to your virtualenv, which is:

    /home/your_username/myvenv
    
Scroll down and click Reload your web app.

Step 4: (Optional) Check your WSGI file
Usually, PythonAnywhere automatically activates your virtualenv if you set it in the Web tab.

---

### 👤 Author

Pranab Mahata(Python & Web Enthusiast)

🔗 GitHub: [@rnccsstudent](github.com/rnccsstudent)

