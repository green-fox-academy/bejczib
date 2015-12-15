from random import randint

class Character:
    def __init__(self, name='Anon', dexterity=0, health=0, luck=0):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def roll_luck(self):
        self.luck = randint(1,6) + 6

    def roll_health(self):
        self.health = randint(1,6) + randint(1,6) + 12

    def roll_dexterity(self):
        self.dexterity = randint(1,6) + 6


