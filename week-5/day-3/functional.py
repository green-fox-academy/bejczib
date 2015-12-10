
class Character:
    def __init__(self, health = 20, armor = 20):
        self._health = health
        self._armor = armor
        self._is_alive = True


    def suffer_damage(self,damage):
        suffered_damage = self._health + self._armor - damage

        if suffered_damage < 1:
            self._is_alive= False

    def heal(self, heal):
        self._health += heal

    def get_health(self):
        return self._health

    def is_alive(self):
        return self._is_alive

def handle_events(eventlist):
    damage_events = list(filter(lambda x: x['type'] == 'damage', eventlist))
    heal_events = list(filter(lambda x: x['type'] == 'heal', eventlist))

    list(map(lambda event: event['character'].heal(event['size']), heal_events))
    list(map(lambda event: event['character'].suffer_damage(event['size']), damage_events))

# def handle_events(eventlist):
#     event_handlers = {
#         'damage': apply_Damage,
#         'heal': apply_heal
#     }
#     list(map(lamdba event: event_handlers[event['type']](event), eventlist))








def filter_array(array):
    return list(filter(lambda x : x % 3 == 0, array))

def adder(array):
    return list(map(lambda x : x + 1, array))
