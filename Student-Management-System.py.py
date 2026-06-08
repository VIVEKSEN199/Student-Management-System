import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Name: "),
        "course": input("Enter Course: "),
        "marks": input("Enter Marks: ")
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")

def view_students():
    students = load_students()

    if not students:
        print("No Records Found")
        return

    for student in students:
        print("-" * 40)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])

def search_student():
    students = load_students()

    sid = input("Enter Student ID to Search: ")

    for student in students:
        if student["id"] == sid:
            print(student)
            return

    print("Student Not Found")

def update_student():
    students = load_students()

    sid = input("Enter Student ID to Update: ")

    for student in students:
        if student["id"] == sid:
            student["name"] = input("New Name: ")
            student["course"] = input("New Course: ")
            student["marks"] = input("New Marks: ")

            save_students(students)
            print("Record Updated Successfully!")
            return

    print("Student Not Found")

def delete_student():
    students = load_students()

    sid = input("Enter Student ID to Delete: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)

            save_students(students)
            print("Record Deleted Successfully!")
            return

    print("Student Not Found")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")