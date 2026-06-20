from Sign_up_and_login import student_id
from storage import give_data

class student():
    def __init__(self):
        try:
            self.Student_id = student_id
            self.Name = input("Enter your name:")
            self.Class = int(input("Enter your class:"))
            self.Age = int(input("Enter your age:"))
            self.Height = int(input("Enter your height(cm):"))
            self.Blood_group = input("Enter your Blood group:")
            
        except ValueError:
            print("Please enter correct numeric value")
            
        except Exception as e:
            print("Unexpected error:", e)
            
        student_data = {
            "Student id":self.Student_id,
            "Name":self.Name,
            "Class":self.Class,
            "Age":self.Age,
            "Height":self.Height,
            "Blood group":self.Blood_group
            }
        give_data(student_data)
