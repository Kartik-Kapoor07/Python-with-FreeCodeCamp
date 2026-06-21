import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")


class Notes:
    @staticmethod
    def ask_user(student_class):
        subject = input("Enter (1) for Science or (2) for Maths: ")
        chapter = input("Enter (1) for Chapter 1 or (2) for Chapter 2: ")

        subjects = {
            "1": "Science",
            "2": "Maths"
        }

        if student_class not in [8, 9, 10]:
            print("Notes are available only for class 8, 9, and 10.")
            return

        if subject not in subjects or chapter not in ["1", "2"]:
            print("Invalid subject or chapter choice.")
            return

        file_path = os.path.join(
            NOTES_DIR,
            f"Class {student_class}",
            subjects[subject],
            f"Chapter {chapter}.pdf"
        )

        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            print("This note file does not exist.")
