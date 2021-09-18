class Thing:
    def __init__(self, name, defense, attack, health):
        if defense > 0.1 or defense < 0:
            raise ValueError('Неверное значение защиты')
        if attack > 100 or attack < 0:
            raise ValueError('Неверное значение атаки')
        if health > 100 or health < 0:
            raise ValueError('Неверное значение здоровья')
        self.name = str(name)
        self.defense = float(defense)
        self.attack = float(attack)
        self.health = float(health)


def sort_key(thing):
    return thing.defense
