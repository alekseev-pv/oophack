from person import Person


class Paladin(Person):
    spec_name = 'Paladin'

    def __init__(self, name, attack, defense, hp, speed, point):
        super().__init__(name, attack, defense, hp, speed, point)
        self.final_hp = hp * 2
        self.final_protection = self.final_protection * 2
        self.radius_attack = 4


class Warrior(Person):
    spec_name = 'Warrior'

    def __init__(self, name, attack, defense, hp, speed, point):
        super().__init__(name, attack, defense, hp, speed, point)
        self.final_attack *= 2
        self.speed = round(self.speed * 1.03)
        self.radius_attack = 6
