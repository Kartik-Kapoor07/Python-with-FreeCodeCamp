class Bank_account:
    def __init__(self,onwer,bank_balance):
        self.onwer = onwer
        self.bank_balance = bank_balance
    
    @property
    def Balance(self):
        print(f"Your name is {self.onwer} and your bank_balance is {self.bank_balance}.")
    
    @Balance.setter
    def Balance(self,add_balance):
        if self._is_valid_amount(add_balance) > 0: # used is valid to know weather the amount is valid or not
            self.bank_balance += add_balance
            self.__log_transaction("Deposit", add_balance)#used log transaction 
        else:
            print("Your add_balance should be an positive integer")
            
    def _is_valid_amount(self,amount):# underscore before the is make it protected
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):# doulbe underscore before log make it private and protected
        print(f"Logging {transaction_type} of {amount}. New balance: {self.Balance}")
            
    @staticmethod
    def is_valid_interest(rate):
        return (0 < rate) and (rate <= 5)
    
account1 = Bank_account("Kartik", 1000)
account2 = Bank_account("Rahul", 2500)

account1.Balance = 3500
