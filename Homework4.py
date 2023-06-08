from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self.balance = 0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_available_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

# Usage example
savings_account = SavingsAccount()
savings_account.deposit(1000)
savings_account.withdraw(500)
print("Available balance:", savings_account.get_available_balance())

current_account = CurrentAccount()
current_account.deposit(2000)
current_account.withdraw(1500)
print("Available balance:", current_account.get_available_balance())