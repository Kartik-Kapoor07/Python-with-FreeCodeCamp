import json
import os

# Dump data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "students.json")


def load_data():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as file:
        return json.load(file)


def give_data(student_data):
    students = load_data()

    for index, student in enumerate(students):
        if student["Student id"] == student_data["Student id"]:
            students[index] = student_data
            break
    else:
        students.append(student_data)

    with open(FILE, "w") as file:
        json.dump(students, file, indent=4)


def get_student_by_id(student_id):
    students = load_data()

    for student in students:
        if student["Student id"] == student_id:
            return student

    return None
