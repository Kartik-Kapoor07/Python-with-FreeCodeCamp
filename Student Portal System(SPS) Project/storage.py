import json
import os

# Dump data

FILE = "students.json"
def give_data(student_data):
    if not os.path.exists(FILE):
        with open(FILE, "w") as file:
            json.dump({student_data}, file, indent=4)
            
    elif os.path.exists(FILE):
        with open(FILE, "w") as file:
            json.dump({student_data}, file, indent=4)