# creating class,objects,giving atribute and using other class data in dog class

class Onwer:
    def __init__(self, Name, Adress, Phone_Number):
        self.Name = Name
        self.Adress = Adress
        self.Phone_Number = Phone_Number
        
class Dog:
    def __init__(self, Dog_name, Breed, Dog_onwer):
        self.Dog_name = Dog_name        
        self.Breed = Breed        
        self.Dog_onwer = Dog_onwer        
    
    def Dog_details(self):
        print(f"The onwer details are:\nName:{self.Dog_onwer.Name}, \nAdress:{self.Dog_onwer.Adress}, \nPhone number:{self.Dog_onwer.Phone_Number}\n")
        print(f"The dog details are: \nName:{self.Dog_name} \nBreed:{self.Breed}")

onwer1 = Onwer("Kartik", "167 Model Town,delhi", "999-888-666") 
Dog1 = Dog("Charlie", "Golden Retriever", onwer1)

Dog1.Dog_details()
