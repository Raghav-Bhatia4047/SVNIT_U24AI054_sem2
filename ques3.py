class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance=0):
        if account_number in self.accounts:
            print(f"Account {account_number} already exists.")
        else:
            self.accounts[account_number] = {
                'customer_name': customer_name,
                'balance': initial_balance
            }
            print(f"Account for {customer_name} created successfully.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number]['balance'] += amount
                print(f"Deposited ${amount} into account {account_number}. New balance: ${self.accounts[account_number]['balance']}")
            else:
                print("Deposit amount must be positive.")
        else:
            print(f"Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance'] and amount > 0:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {account_number}. New balance: ${self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print(f"Account {account_number} not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: ${self.accounts[account_number]['balance']}")
        else:
            print(f"Account {account_number} not found.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account]['balance'] >= amount and amount > 0:
                self.accounts[from_account]['balance'] -= amount
                self.accounts[to_account]['balance'] += amount
                print(f"Transferred ${amount} from account {from_account} to account {to_account}.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("One or both accounts not found.")

def void():
      print("""Enter 
    0 to exit
    1 to create account
    2 to deposit
    3 to withdraw
    4 to check balance
    5 to tranfer""")
bank = Bank()
while(1):
    void()
    k=int(input())
    match(k):
        case 0 : exit(1)
        case 1 :
                data=int(input("Enter acc number: "))
                name=input("Enter name: ")
                bank.create_account(data,name)
                
        case 2 : 
                data=int(input("enter acc number: "))
                amount=int(input("enter amount: "))
                bank.deposit(data,amount)
        case 3 : 
                data=int(input("enter acc number: "))
                amount=int(input("enter amount: "))
                bank.withdraw(data,amount)
        case 4 : 
               data=int(input("enter acc number: "))
               bank.check_balance(data)
        case 5 :
              fro=int(input("enter your acc number: "))
              to=int(input("enter acc number in which you have to transfer amount: "))
              amount=int(input("enter amount: "))
              bank.transfer(fro,to,amount)
            
