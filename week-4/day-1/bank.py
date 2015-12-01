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

    def transfer(self, target, money):
        try:
            if self.ballance > money:
                target.receive(money)
                self.pay(money)
            else:
                raise Exception('Nagy turot Oreg, nincs loveeee!')
        except Exception:
                print('Nagy turot Oreg, nincs annyi penzed!')

client1 = BankAccount('Balint', 0)
client2 = BankAccount('Feri', 500)

client1.transfer( client2, 50)
