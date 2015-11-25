class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self, name, balance, amount):
        self.balance += amount
        return self.balance

    def widthdraw(self, name, balance, amount):
        self.balance -= amount
        return self.balance

account1 = BankAccount('Lisa', 20)
