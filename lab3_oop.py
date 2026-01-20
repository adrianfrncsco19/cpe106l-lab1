# Week 3: Bank Account Class (OOP)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Create an account object
account = BankAccount("John", 1000)

# Perform transactions
account.deposit(500)
account.withdraw(300)

# Display final balance
print(account.balance)
