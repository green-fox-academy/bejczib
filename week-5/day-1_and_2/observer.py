class Warrior:
    def __init__(self, name):
        self.companions = []
        self.hp = 100
        self.name = name
        self.fly = True

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

    def curse(self, opponent):
        opponent.cursed()

    def cursed(self):
        self.name += '_Cursed'
        for companion in self.companions:
            companion.notify('curse', self)

    def do_not_fly(self, opponent):
        opponent.i_can_not_fly()

    def i_can_not_fly(self):
        self.fly = False
        for companion in self.companions:
            companion.notify('no wings', self)

    def heal(self, hp):
        self.hp += hp

    def remove_curse(self):
        self.name = 'alma'

    def restore_fly(self):
        self.fly = True

class Healer:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(10)
        elif type == 'curse':
            warrior.remove_curse()
        elif type == 'no wings':
            warrior.restore_fly()


rabbit = Warrior('rabbit')
wolf = Warrior('wolf')
shaman = Healer()
other_healer = Healer()

rabbit.join(shaman)
wolf.join(other_healer)

wolf.strike(rabbit)

rabbit.curse(wolf)

rabbit.do_not_fly(wolf)

print(wolf.fly)
print(rabbit.hp)
print(wolf.name)
