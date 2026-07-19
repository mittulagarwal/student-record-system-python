students = []

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    age = input("Enter age: ")

    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists!")
            return

    try:
        int(age)
    except ValueError:
        print("Age must be a number!")
        return

    students.append({"name": name, "roll": roll, "age": age})
    print("Student added successfully.")

def view_students():
    print("\n--- All Students ---")
    if not students:
        print("No records found.")
        return
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Age: {s['age']}")

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Age: {s['age']}")
            return
    print("Student not found.")

def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input(f"Enter new name ({s['name']}): ") or s["name"]
            new_age = input(f"Enter new age ({s['age']}): ")
            if new_age:
                try:
                    int(new_age)
                    s["age"] = new_age
                except ValueError:
                    print("Invalid age. Keeping original.")
            print("Student updated successfully.")
            return
    print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully.")
            return
    print("Student not found.")

def main():
    while True:
        print("\n=== Student Record System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
