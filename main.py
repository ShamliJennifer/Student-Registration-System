"""Student Registration & Contact Intelligence System.

Author: S. Shamli Jennifer
"""

from pathlib import Path

from analytics import generate_report
from loader import load_contacts, save_contacts
from validator import validate_contact

DATA_FILE = Path(__file__).with_name("contacts.csv")
OUTPUT_FILE = Path(__file__).with_name("students_clean.csv")


def find_student(students: list[dict], phone: str):
    return next((item for item in students if item["phone"] == phone), None)


def view_students(students: list[dict]) -> None:
    print("\n--- STUDENT RECORDS ---")
    if not students:
        print("No student records found.")
        return
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']} | {student['phone']} | {student['email']}")


def search_student(students: list[dict]) -> None:
    term = input("Enter name, phone, or email to search: ").strip().casefold()
    matches = [
        item for item in students
        if term in item["name"].casefold()
        or term in item["phone"]
        or term in item["email"].casefold()
    ] if term else []
    if matches:
        view_students(matches)
    else:
        print("No matching student found.")


def register_student(students: list[dict]) -> None:
    name = input("Enter student name: ").strip()
    phone = input("Enter 10-digit phone number: ").strip()
    email = input("Enter email address: ").strip()
    valid, message = validate_contact(name, phone, email)
    if not valid:
        print("Registration failed:", message)
        return
    if any(item["phone"] == phone for item in students):
        print("Registration failed: phone number already exists.")
        return
    if any(item["email"].casefold() == email.casefold() for item in students):
        print("Registration failed: email already exists.")
        return
    students.append({"name": name, "phone": phone, "email": email})
    print("Student registered successfully.")


def update_student(students: list[dict]) -> None:
    old_phone = input("Enter the current phone number of the student: ").strip()
    student = find_student(students, old_phone)
    if student is None:
        print("Student not found.")
        return

    name = input("Enter updated name: ").strip()
    phone = input("Enter updated phone number: ").strip()
    email = input("Enter updated email: ").strip()
    valid, message = validate_contact(name, phone, email)
    if not valid:
        print("Update failed:", message)
        return

    for other in students:
        if other is not student:
            if other["phone"] == phone:
                print("Update failed: phone number already exists.")
                return
            if other["email"].casefold() == email.casefold():
                print("Update failed: email already exists.")
                return

    student.update({"name": name, "phone": phone, "email": email})
    print("Student updated successfully.")


def delete_student(students: list[dict]) -> None:
    phone = input("Enter the phone number of the student to delete: ").strip()
    student = find_student(students, phone)
    if student is None:
        print("Student not found.")
        return
    students.remove(student)
    print("Student deleted successfully.")


def main() -> None:
    students, import_summary = load_contacts(str(DATA_FILE))
    print("\n--- DATA IMPORT SUMMARY ---")
    print(f"Rows read: {import_summary['total']}")
    print(f"Accepted: {import_summary['accepted']}")
    print(f"Invalid: {import_summary['invalid']}")
    print(f"Duplicates: {import_summary['duplicates']}")

    actions = {
        "1": lambda: view_students(students),
        "2": lambda: search_student(students),
        "3": lambda: register_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: print(generate_report(students, import_summary)),
    }

    while True:
        print("\n====== STUDENT REGISTRATION SYSTEM ======")
        print("1. View students")
        print("2. Search student")
        print("3. Register student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Analytics report")
        print("7. Save and exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice in actions:
            actions[choice]()
        elif choice == "7":
            save_contacts(students, str(OUTPUT_FILE))
            print(f"Records saved to {OUTPUT_FILE.name}. Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
