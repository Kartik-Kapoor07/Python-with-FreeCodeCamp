import re
import json
import os 
from Password_manager import verify
from Id_generator import get_student_id

FILE = "C:\\Users\\karti\\Music\\Python-with-FreeCodeCamp\\Student Portal System(SPS) Project\\Password.json"
def sign_in():
    Username = input("Enter your username:")
    
    while True:
        password = input("Enter your password")
        if len(password) < 8:
            print("Password must be at least 8 characters long")

        if not re.search(r"[A-Z]", password):
            print("Add at least 1 uppercase letter (A-Z)")

        if not re.search(r"[a-z]", password):
            print("Add at least 1 lowercase letter (a-z)")

        if not re.search(r"[0-9]", password):
            print("Add at least 1 number (0-9)")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            print("Add at least 1 special character (!@#$...)")
        
        else:
            print("Password Accepted")
            student_id = get_student_id()
            User_pass = {
                "Student id":student_id,
                "Username":Username,
                "Password":password
            }
            if not os.path.exists(FILE):
                with open(FILE, "w") as file:
                    json.dump({User_pass}, file, indent=4)
            elif os.path.exists(FILE):
                with open(FILE, "a") as file:
                    json.dump({User_pass}, file, indent=4)


def log_in():
    Username = input("Enter your username:")
    password = input("Enter your password:")
    
    with open("Student Portal System(SPS) Project\Json\Security_details.jsong","r") as file:
        json_object = json.read(file)
        if Username not in json_object:
            raise TypeError("Your input is wrong!")
        
        user_data = json_object[Username]
        salt = user_data["salt"]
        stored_hash = user_data["hash"]
        
        if verify(stored_hash,password,salt):
            print("The username and password is correct you are logged in")