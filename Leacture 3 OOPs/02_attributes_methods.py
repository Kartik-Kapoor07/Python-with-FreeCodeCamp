# Accessing and modifying data in objects

class user:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def say_hi_to_user(self,user):
        print(f"sending messsage to {user.email}: Hi {user.username}, its's {self.username}")
        
user1 = user("Kartik", "Kartik@gmail.com", 123)
user2 = user("kapoor", "kapoor@gmail.com", 871)

user1.say_hi_to_user(user2)

print(user2.email)
user2.email = "xyz@gmail.com"
print(user2.email)
