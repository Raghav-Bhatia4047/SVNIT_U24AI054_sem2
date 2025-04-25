class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")

account = BankAccount(123456, 500)
account.deposit(200)
account.withdraw(100)
account.display()
