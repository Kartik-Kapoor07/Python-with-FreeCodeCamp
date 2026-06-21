from storage import give_data

class Student:
    def __init__(self, student_id):
        try:
            self.Student_id = student_id
            self.Name = input("Enter your name: ")
            self.Class = int(input("Enter your class: "))
            self.Age = int(input("Enter your age: "))
            self.Height = int(input("Enter your height(cm): "))
            self.Blood_group = input("Enter your Blood group: ")
            
        except ValueError:
            print("Please enter correct numeric value")
            return
            
        except Exception as e:
            print("Unexpected error:", e)
            return
            
        student_data = {
            "Student id":self.Student_id,
            "Name":self.Name,
            "Class":self.Class,
            "Age":self.Age,
            "Height":self.Height,
            "Blood group":self.Blood_group
            }
        give_data(student_data)


student = Student
