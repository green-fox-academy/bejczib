from random import randint

class Character:
    def __init__(self, name='Anon', dexterity=0, health=0, luck=0, potion= 0):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.potion = potion

    def roll_luck(self):
        self.luck = randint(1,6) + 6

    def roll_health(self):
        self.health = randint(1,6) + randint(1,6) + 12

    def roll_dexterity(self):
        self.dexterity = randint(1,6) + 6


#.... later..

# class PotionOfHealth:
#     def __init__(self, character):
#         self.character = character

#     def add_health(self, character):
#         return self.character.health + 15
