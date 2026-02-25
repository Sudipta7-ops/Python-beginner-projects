# Project 10: Simple Note App
# Saves user notes to a text file for persistent storage
# Built with Python using file handling (open, write, append)

def save_note(note_text):
    with open("notes.txt", "a") as file:
        file.write(note_text + "\n")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            print("\n--- Your Saved Notes ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
        else:
            print("No notes saved yet.")
    except FileNotFoundError:
        print("No notes saved yet.")

print("Welcome to Simple Note App")
print("1. Add Note")
print("2. View Notes")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    note = input("Enter your note: ")
    save_note(note)
    print("Your note has been saved.")
elif choice == "2":
    view_notes()
else:
    print("Invalid option.")
