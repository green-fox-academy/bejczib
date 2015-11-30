class BankAccount(object):
    def __init__(self, name, ballance):
        self.name = name
        self.ballance = ballance

    def pay(self, money):
        self.ballance -= money

    def receive(self, money):
        self.ballance += money

    def print_balance(self):
        return self.name, self.ballance

client1 = BankAccount('Balint', 100)

client1.pay(20)
client1.receive(50)
print(client1.print_balance())
