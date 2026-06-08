# Student-Management-System
# 🎓 Student Management System (CRUD Application)

A fully interactive, terminal-based *Student Management System* built using Python. This project demonstrates backend data management concepts by implementing full *CRUD (Create, Read, Update, Delete)* operations with persistent JSON file storage.

---

## 🚀 Key Features

- *➕ Add Student:* Inserts a new student record with a unique ID, Name, Course, and Marks.
- *📋 View All Students:* Fetches and displays all stored student records in a clean, readable format.
- *🔍 Search Student:* Instantly searches and finds a student's profile using their unique Student ID.
- *🔄 Update Record:* Allows modifications to an existing student's Name, Course, or Marks.
- *❌ Delete Record:* Removes a student's profile permanently from the database.

---

## 🛠️ Tech Stack & Concepts Used

* *Language:* Python 3
* *Database/Storage:* JSON File Handling (json module) for permanent data storage.
* *File System Verification:* Built-in os module to safely handle file path existence and prevent crashes.
* *Control Flow:* Advanced loops (while True) and conditional logic (if-elif-else) for seamless user experience.

---

## 📂 Project Structure & Logic

1. *load_students()*: Checks if students.json exists using os.path.exists(). If found, parses JSON data into a Python list; otherwise, initializes an empty list.
2. *save_students()*: Converts Python data structures back into structured JSON format and writes to disk with indent=4 for human-readable formatting.
3. *Main Menu Loop*: A continuous loop that acts as the user interface in the terminal, accepting choices from 1 to 6.

---

## 💻 How To Run

1. Clone or download the Student-Management-System.py file.
2. Open your terminal/command prompt and run:
   ```bash
   python Student-Management-System.py
