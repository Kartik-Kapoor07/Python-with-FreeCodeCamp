# Inheritance allows a class to reuse features of another class and child class uses parent class features

class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")
        
class car(vehicle):
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
        
class bike(vehicle):
    def __init__(self, brand,model,year, speed):
        super().__init__(brand, model, year)
        self.speed = speed

car1 = car("Ford", "Mustang", 1964, 2, 4)
bike1 = bike("Honda", "Activa", 2018, 130)

print(car1.__dict__)