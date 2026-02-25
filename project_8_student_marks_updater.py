# Project 8: Student Marks Updater
# Manages a student records system with add, view, update, and delete features
# Built with Python using dictionaries, functions, and a while loop

students = {}

def show_menu():
    print("\n--- Student Marks Updater ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students[name] = marks
    print(f"{name}'s marks added successfully.")

def view_students():
    if not students:
        print("No student records available yet.")
    else:
        print("\nStudent Records:")
        for name, marks in students.items():
            print(f"  {name}: {marks}")

def update_marks():
    name = input("Enter student name to update: ")
    if name in students:
        new_marks = float(input("Enter new marks: "))
        students[name] = new_marks
        print(f"{name}'s marks updated to {new_marks}.")
    else:
        print(f"Student '{name}' not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        students.pop(name)
        print(f"{name}'s record deleted.")
    else:
        print(f"Student '{name}' not found.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
