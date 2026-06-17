class user:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.__password = password 
        
    def get_email(self):
        return self._email
        
    def set_email(self,new_email):
        self._email = new_email
        
    def say_hi_to_user(self,user):
        print(f"sending messsage from {self._email} to {user._email}: Hi {user.username}, its's {self.username}")
        
user1 = user("Kartik", "Kartik@gmail.com", 123)
user2 = user("kapoor", "kapoor@gmail.com", 871)

print(user1.get_email())
user1.set_email("alex@gmail.com")

user1.say_hi_to_user(user2)
