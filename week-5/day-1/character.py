class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def drink_potion(self):
        self.hp += 10

    def strike(self, name):
        name.hp -= self.damage

    def get_status(self):
        sdf
        sdf
        return status

    def print_status(self):
        pint(self.get_status())
