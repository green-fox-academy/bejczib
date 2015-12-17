import json

class Save:

    def save(name,item):
        filename = open(name + '.json', 'w')
        json.dump(item, filename)
        filename.close()
