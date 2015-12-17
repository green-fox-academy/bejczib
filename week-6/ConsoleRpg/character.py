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

    def try_my_luck(self):
        return randint(1,6) * 2





    def save(self, name, item):
        filename = open(name + '.json', 'w')
        json.dump(item, filename)
        filename.close()

    def make_dict(self):
        return {'Name': self.name,
                'Dexterity': self.dexterity,
                'Health': self.health,
                'Current Health': self.current_health,
                'Luck': self.luck,
                'Current Luck': self.current_luck,
                'Inventory': self.inventory
                }

    def list_jsons(self):
        jsons = []
        for file in os.listdir():
            if file.endswith(".json"):
                jsons.append(file)
        for item in jsons:
            print(item.split('.')[0])

    def load(self, saved_file):
        loaded = []
        filename = open(saved_file + '.json', 'r')
        try:
            loaded = json.load(filename)
        except Exception:
            pass
        filename.close()

        return loaded

    def dict_to_player(self, saved_dict):
        self.name = saved_dict['Name']
        self.dexterity = saved_dict['Dexterity']
        self.luck = saved_dict['Luck']
        self.current_luck = saved_dict['Current Luck']
        self.health = saved_dict['Health']
        self.current_health = saved_dict['Current Health']
        self.inventory = saved_dict['Inventory']


class Fight(Character):
    def is_hit(self):
        if player.roll_strength() > monster.roll_strength():
            return True
        elif player.roll_strength() < monster.roll_strength():
            return False
        else:
            self.is_hit()

    def after_strike(self):
        if self.is_hit:
            monster.current_health =- 2
        else:
            player.current_health =- 2

    def try_luck(self):
        if self.is_hit()
        if player.try_my_luck() < player.current_luck:
            monster.current_health =- 4
            player.current_luck =- 1
        else:
            monster.current_health =- 1


player = Character()
monster = Character()
fight = Fight()
