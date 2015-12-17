from random import randint
import json
import os

class Character:
    def __init__(self, name='Lilla', dexterity=0, health=0, luck=0, inventory = ["Sword", "Leather Armor", ""]):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.inventory = inventory

    def roll_luck(self):
        self.luck = randint(1,6) + 6

    def roll_health(self):
        self.health = randint(1,6) + randint(1,6) + 12

    def roll_dexterity(self):
        self.dexterity = randint(1,6) + 6

    def get_inventory(self, choice):
        self.inventory[2] = choice

    def strike_roll(self):
        return self.dexterity + randint(1,6) + randint(1,6)

    def is_win(self, opponet):
        return self.strike_roll() > opponet.strike_roll()

    def save(self, name, item):
        filename = open(name + '.json', 'w')
        json.dump(item, filename)
        filename.close()

    def make_dict(self):
        return {'name': self.name,
                'Dexterity': self.dexterity,
                'Health': self.health,
                'Luck': self.luck,
                'Inventory': self.inventory
                }

    def list_jsons(self):
        jsons = []
        for file in os.listdir():
            if file.endswith(".json"):
                jsons.append(file)
        for item in jsons:
            print(item.split('.')[0])
        return item  #just for avoid None

    def load(self, saved_file):
        loaded = []
        filename = open(saved_file + '.json', 'r')
        try:
            loaded = json.load(filename)
        except Exception:
            pass
        filename.close()

        return loaded






#.... later..

# class PotionOfHealth:
#     def __init__(self, character):
#         self.character = character

#     def add_health(self, character):
#         return self.character.health + 15
