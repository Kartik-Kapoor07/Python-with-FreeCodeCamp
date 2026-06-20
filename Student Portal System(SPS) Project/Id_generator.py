import json
import os

FILE = "C:\\Users\\karti\\Music\\Python-with-FreeCodeCamp\\Student Portal System(SPS) Project\\meta.json"

def get_student_id():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({"last_id": 100000}, f, indent=4)
            
    elif  os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

        counter = data["last_id"]   
        counter = counter + 1       

        data["last_id"] = counter   

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)