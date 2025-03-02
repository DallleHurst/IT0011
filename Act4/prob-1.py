import json

FILENAME = "students.json"
students = [
    (100001, ("John", "Doe"), 85, 90),
    (100002, ("Jane", "Smith"), 78, 88),
    (100003, ("Alice", "Johnson"), 92, 85),
]

def save_file(filename=FILENAME):
    with open(filename, "w") as file:
        json.dump(students, file)
    print(f"Records saved as {filename}!")

def load_file():
    global students
    try:
        with open(FILENAME, "r") as file:
            students = json.load(file)
        print("Records loaded successfully!")
    except FileNotFoundError:
        print("No existing file found.")

def show_all_students():
    for student in students:
        print(student)

def order_by_last_name():
    for student in sorted(students, key=lambda s: s[1][1]):
        print(student)

def order_by_grade():
    for student in sorted(students, key=lambda s: s[2] * 0.6 + s[3] * 0.4, reverse=True):
        print(student)

def show_student_record(student_id):
    for student in students:
        if student[0] == student_id:
            print(student)
            return
    print("Student not found!")

def add_record():
    student_id = int(input("Enter Student ID (6-digit): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Student added successfully!")

def edit_record(student_id):
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Student record updated successfully!")
            return
    print("Student not found!")

def delete_record(student_id):
    global students
    students = [s for s in students if s[0] != student_id]
    print("Student record deleted!")

def main():
    actions = {
        "1": load_file,
        "2": save_file,
        "3": lambda: save_file(input("Enter new filename: ")),
        "4": show_all_students,
        "5": order_by_last_name,
        "6": order_by_grade,
        "7": lambda: show_student_record(int(input("Enter Student ID: "))),
        "8": add_record,
        "9": lambda: edit_record(int(input("Enter Student ID to edit: "))),
        "10": lambda: delete_record(int(input("Enter Student ID to delete: "))),
        "11": exit
    }
    
    while True:
        print("\nStudent Record Management System")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action.replace('_', ' ').title()}")
        choice = input("Enter your choice: ")
        actions.get(choice, lambda: print("Invalid choice! Please try again."))()

if __name__ == "__main__":
    main()
