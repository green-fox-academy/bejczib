from character import Character

class Cleric(Character):
    pass

    def heal(self, other):
        other.hp += 10
