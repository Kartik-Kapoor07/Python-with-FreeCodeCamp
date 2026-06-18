# Encapsulation = Hiding data and controlling how it is accessed.we are already using it without knowing in previous files
class Bankaccount:
    def __init__(self,Onwer,Bank_balance):
        self.onwer = Onwer
        self.Bank_balance = 0
        self._Is_accetable_Bank_balance(Bank_balance)
        
    def deposit(self,amount):
        self._Is_accetable_Bank_balance(amount)
        
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Amount should be an negtive integer")
        elif amount > self.Bank_balance:
            raise ValueError("Not suffient funds")
        else:
            self.Bank_balance -=amount
            self.__logs("Withdraw",amount) 

        
    def _Is_accetable_Bank_balance(self,amount):
        if amount <= 0:
            raise ValueError("Amount should be an positive integer")
        else:
            self.Bank_balance +=amount
            self.__logs("Deposit",amount)
            
    def __logs(self,transaction,amount):
        print(f"Logging {transaction} of {amount}. New balance: {self.Bank_balance}")
        
    def show_balance(self):
        print(f"Current balance: {self.Bank_balance}")

account1 = Bankaccount("Kartik", 1000)
account2 = Bankaccount("Rahul", 2500)

account1.deposit(350)
account2.withdraw(900)