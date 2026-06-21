import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "meta.json")

def get_student_id():
    if not os.path.exists(FILE):
        counter = 100001
        with open(FILE, "w") as f:
            json.dump({"last_id": counter}, f, indent=4)
            
    else:
        with open(FILE, "r") as f:
            data = json.load(f)

        counter = data["last_id"]   
        counter = counter + 1       

        data["last_id"] = counter   

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    return counter
