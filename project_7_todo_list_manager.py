# Project 7: To-Do List Manager
# A simple terminal-based task manager with add, view, and remove features
# Built with Python using lists, functions, and a while loop

todo_list = []

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet. Add a task to get started!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"  {i}. {task}")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f'Task "{task}" added successfully.')

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            removed = todo_list.pop(task_num - 1)
            print(f'Task "{removed}" removed successfully.')
        except (IndexError, ValueError):
            print("Invalid selection. Please enter a valid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
