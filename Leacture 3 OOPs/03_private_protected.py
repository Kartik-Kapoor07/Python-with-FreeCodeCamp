# Protected and private data attribute

class user:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # the underscore make the data protected
        self.__password = password # the double underscore make the data protected and private and if we  try to access that error will be thrown 
        
    def say_hi_to_user(self,user):
        print(f"sending messsage to {user.email}: Hi {user.username}, its's {self.username}")
        
user1 = user("Kartik", "Kartik@gmail.com", 123)
user2 = user("kapoor", "kapoor@gmail.com", 871)

print(user1._email) # The correct output will come even if email is protected in python unlike other programming lan like c++ it will not throw an error

