# Property help not to write the () and dont repeat names

class user:
    def __init__(self, username, email, password, isadmin=False): 
        self.username = username
        self._email = email 
        self.__password = password
        self.isadmin = isadmin 
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,new_email):
        
        if new_email[-10:] == "@gmail.com":# validation check
            self._email = new_email
        else:
            print("Invalid email adress!")
        
    def say_hi_to_user(self,user):
        print(f"sending messsage from {self._email} to {user._email}: Hi {user.username}, its's {self.username}")
        
user1 = user("Kartik", "Kartik@gmail.com", 123)
user2 = user("kapoor", "kapoor@gmail.com", 871)

user1.email = "Shreya@gmail.com"
print(user1.email)

user1.say_hi_to_user(user2)