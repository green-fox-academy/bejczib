class Arena:
    def strike(self):
        pass
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(10)

class Warrior:
    def __init__(self):
        self.companions= [Arena()]
        self.hp = 100

    def strike(self, opponent):
        opponent.inflict_damage(15)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

    def heal(self, hp):
        self.hp += hp

warrior = Warrior()
opponent = Warrior()

warrior.strike(opponent)
print(opponent.hp)
