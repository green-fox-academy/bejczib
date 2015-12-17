import json
import os
from character import *

class Load:
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
        player.name = saved_dict['Name']
        player.dexterity = saved_dict['Dexterity']
        player.luck = saved_dict['Luck']
        player.current_luck = saved_dict['Current Luck']
        player.health = saved_dict['Health']
        player.current_health = saved_dict['Current Health']
        player.inventory = saved_dict['Inventory']

load = Load()
