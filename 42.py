#42.Write a Python class that implements a 
# simple bank account with deposit and withdraw methods.
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Name of the account holder
        self.balance = initial_balance  # Initial balance (default is 0)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check the balance
    def get_balance(self):
        return self.balance

# Example usage
account_holder = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_holder, initial_balance)

# Example deposits and withdrawals
account.deposit(500)  # Deposit 500
account.withdraw(200)  # Withdraw 200
account.withdraw(1000)  # Try to withdraw more than the balance

# Print final balance
print(f"Final balance: {account.get_balance()}")

