from person import Person


class Paladin(Person):
    def __init__(self, name, attack, defense, hp):
        super().__init__(name, attack, defense, hp)
        self.final_hp = hp * 2
        self.final_protection = self.final_protection * 2
        self.spec_name = 'Paladin'


class Warrior(Person):
    def __init__(self, name, attack, defense, hp):
        super().__init__(name, attack, defense, hp)
        self.final_attack *= 2
        self.spec_name = 'Warrior'
