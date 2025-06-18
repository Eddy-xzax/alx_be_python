class BankAccount:
 def __init__(self,account_balance):
    self.account_balance = account_balance 
 def deposit(self , amount):
    self.account_balance += amount
    return self.account_balance
 def withdraw(self , amount):
    if amount <= self.account_balance:
        self.amount_balance -= amount
        return True
    else:
        return False
 def display_balance(self):
    print(f"Current balance is: ${self.account_balance: .2f}")
