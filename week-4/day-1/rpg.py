import random

class Character:
    def __init__(self, name, HP, damage):
        self.name = name
        self.HP = HP
        self.damage = damage

    def print_status(self):
        if self.HP <= 0:
            return self.name + ' is dead.'
        else:
            return self.name + ' HP is ' + str(self.HP)

    def drink_potion(self):
        potion = 10
        self.HP += potion

    def strike(self, target):
        target.HP -= self.damage

    def round(self):
        round = 0
        while en.HP >=0 and te.HP >=0 and arch_enemy.HP >= 0:
            en.strike(arch_enemy)
            te.strike(arch_enemy)
            arch_enemy.strike(en)
            arch_enemy.strike(te)
            round += 1
        if en.HP <= 0 or te.HP <= 0 or arch_enemy.HP <= 0:
            print('game over')
            print(en.print_status())
            print(te.print_status())
            print(arch_enemy.print_status())
            print('{} kor allatt gyaktuk le oket'.format(round))


enemies = [
    Character('Bela', random.randint(50,100), random.randint(5,10)),
    Character('Judit', random.randint(50,100), random.randint(5,10)),
    Character('Gyuri', random.randint(50,100), random.randint(5,10)),
    Character('Tojas', random.randint(50,100), random.randint(5,10))
]

arch_enemy = random.choice(enemies)

en = Character('Balint', 100, 10)
te = Character('Peti', 100, 10)

en.round()
