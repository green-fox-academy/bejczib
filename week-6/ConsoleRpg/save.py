import json
from character import *
class Save:
    def save(self, name, item):
        filename = open(name + '.json', 'w')
        json.dump(item, filename)
        filename.close()

    def make_dict(self):
        return {'Name': player.name,
                'Dexterity': player.dexterity,
                'Health': player.health,
                'Current Health': player.current_health,
                'Luck': player.luck,
                'Current Luck': player.current_luck,
                'Inventory': player.inventory
                }

save = Save()
