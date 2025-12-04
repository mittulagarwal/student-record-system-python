# Simple Student Record Management System (Python)

students = []

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    age = input("Enter age: ")

    # check duplicate roll
    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists!")
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
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
