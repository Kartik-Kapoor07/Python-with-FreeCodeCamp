# polymorphism is a concept of the oops

class bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

account1=bankaccount("kartik",1000)
account2=bankaccount("sahil",2000)

account1.deposit(500) # it will return "Deposit of 500 successful. New balance: 1500"
account2.deposit(1000) # it will return "Deposit of 1000 successful. New balance: 3000"

account1.withdraw(200) # it will return "Withdrawal of 200 successful. New balance: 1300"
account2.withdraw(500) # it will return "Withdrawal of 500 successful. New balance: 1500"

# dont understand much because till now i dont start oops and i study or code this because it is a part of leacture1 and i want to complete it first then i will start oops and then i will understand this code better.
