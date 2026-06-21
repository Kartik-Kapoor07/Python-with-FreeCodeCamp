import re
import json
import os 
from Password_manager import generate_salt, hash_password, verify
from Id_generator import get_student_id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "Password.json")


def load_users():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)


def sign_in():
    Username = input("Enter your username: ")
    users = load_users()

    if Username in users:
        print("Username already exists. Please login or choose another username.")
        return None
    
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("Password must be at least 8 characters long")
            continue

        if not re.search(r"[A-Z]", password):
            print("Add at least 1 uppercase letter")
            continue

        if not re.search(r"[a-z]", password):
            print("Add at least 1 lowercase letter")
            continue

        if not re.search(r"[0-9]", password):
            print("Add at least 1 number")
            continue

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            print("Add at least 1 special character")
            continue
        else:
            print("Password Accepted")
            student_id = get_student_id()
            salt = generate_salt()
            users[Username] = {
                "Student id": student_id,
                "salt": salt,
                "hash": hash_password(password, salt)
            }
            save_users(users)
            return student_id


def log_in():
    Username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = load_users()

    if Username not in users:
        print("Username not found.")
        return None

    user_data = users[Username]
    salt = user_data["salt"]
    stored_hash = user_data["hash"]

    if verify(stored_hash, password, salt):
        student_id = user_data["Student id"]
        print("The username and password is correct. You are logged in.")
        return student_id

    print("Wrong password.")
    return None
