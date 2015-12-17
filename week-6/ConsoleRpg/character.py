from random import randint
import json
import os

class Character:
    def __init__(self, name='Lilla', dexterity=0, health=0, luck=0, inventory = ["Sword", "Leather Armor", ""]):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.current_health = health
        self.luck = luck
        self.current_luck = luck
        self.inventory = inventory

    def roll_luck(self):
        self.luck = randint(1,6) + 6

    def roll_health(self):
        self.health = randint(1,6) + randint(1,6) + 12

    def roll_dexterity(self):
        self.dexterity = randint(1,6) + 6

    def get_inventory(self, choice):
        self.inventory[2] = choice

    def roll_strength(self):
        return self.dexterity + randint(1,6) + randint(1,6)

    def roll_try_luck(self):
        return randint(1,6) + randint(1,6)

player = Character()
monster = Character()

