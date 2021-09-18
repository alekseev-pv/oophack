class Thing:
    def __init__(self, name, defense, attack, health):
        if 0 > defense > 0.1:
            raise ValueError
        if 0 > attack > 100:
            raise ValueError
        if 0 > health > 100:
            raise ValueError
        self.name = str(name)
        self.defense = float(defense)
        self.attack = float(attack)
        self.health = float(health)


def sort_key(thing):
    return thing.defense
