# Static atribute:common data for the class and can be used by all objects and functions

class User:
    user_count = 0
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count +=1
        
    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")
        
user1 = User("Shreya", "Shreya@gmail.com")
user2 = User("Kartik", "Kartik@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)

# Static Method:static method dont take other arguments(self) of a class and works independently 

class Bank_account:
    def __init__(self,onwer,bank_balance):
        self.onwer = onwer
        self.bank_balance = bank_balance
    
    @property
    def Balance(self):
        print(f"Your name is {self.onwer} and your bank_balance is {self.bank_balance}.")
    
    @Balance.setter
    def Balance(self,add_balance):
        if add_balance > 0:
            self.bank_balance += add_balance
            print(f"Your bank balance added by {add_balance}.New balance {self.bank_balance}")
        else:
            print("Your add_balance should be an positive integer")
            
    @staticmethod
    def is_valid_interest(rate):
        return (0 < rate) and (rate <= 5)
    
account1 = Bank_account("Kartik", 1000)
account2 = Bank_account("Rahul", 2500)

account1.Balance = 3500

print(Bank_account.is_valid_interest(4.9))
print(Bank_account.is_valid_interest(5.1))

