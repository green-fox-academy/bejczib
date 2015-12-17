from character import *

class Fight:
    def is_hit(self):
        if player.roll_strength() > monster.roll_strength():
            return True
        elif player.roll_strength() < monster.roll_strength():
            return False
        else:
            return self.is_hit()

    def after_strike(self):
        if self.is_hit():
            monster.current_health =- 2
        else:
            player.current_health =- 2

    def try_luck(self):
        if self.is_hit():
            if player.roll_try_luck() < player.current_luck:
                monster.current_health =- 4
                player.current_luck =- 1
            else:
                monster.current_health =- 1
        elif not self.is_hit():
            if player.roll_try_luck() < player.current_luck:
                player.current_health =- 1
                player.current_luck =- 1
            else:
                player.current_health =- 3

fight = Fight()
