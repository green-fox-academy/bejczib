from character import Character

class Wizzard(Character):
    def __init__(self, name, hp, damage, manna):
        super().__init__(name, hp, damage) # this is for inheritance of the constructor of Caracter.
        self.manna = manna

    def strike(self, opponent):
        if self.manna >= 5:
            self.manna -= 5
            opponent.hp -= self.damage *3
        else:
            opponent.hp -= self.damage / 3
