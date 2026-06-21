from Notes import Notes
from Sign_up_and_login import log_in, sign_in
from Student import Student
from storage import get_student_by_id


def main_menu():
    while True:
        print("\n--- Student Portal System ---")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = sign_in()
            if student_id is not None:
                print(f"Your student ID is {student_id}")
                Student(student_id)

        elif choice == "2":
            student_id = log_in()
            if student_id is not None:
                student_dashboard(student_id)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


def student_dashboard(student_id):
    while True:
        print("\n--- Student Dashboard ---")
        print("1. View Profile")
        print("2. Open notes")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(student_id)

        elif choice == "2":
            student = get_student_by_id(student_id)

            if student is None:
                print("Student profile not found. Please create your profile first.")
            else:
                Notes.ask_user(student["Class"])

        elif choice == "3":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


def view_profile(student_id):
    student = get_student_by_id(student_id)

    if student is None:
        print("Student profile not found. Please create your profile first.")
        return

    print("\n--- View Profile ---")
    print(f"Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Height: {student['Height']} cm")
    print(f"Blood Group: {student['Blood group']}")
    print(f"Class: {student['Class']}")
    print(f"Roll Number: {student['Student id']}")


if __name__ == "__main__":
    main_menu()
