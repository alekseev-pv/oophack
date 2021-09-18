import messages


class Person:
    def __init__(self, name, hp, base_ad, base_resist):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.base_ad = base_ad
        self.base_resist = base_resist
        self.items = []

    def set_things(self, things):
        self.items = things

    def final_protection(self) -> float:
        protection = self.base_resist
        for item in self.items:
            protection = protection + item.protection
        return protection

    def final_attack(self) -> float:
        attack = self.base_ad
        for item in self.items:
            attack = attack + item.attack
        return attack

    def defend(self, attacker):
        damage = (
            round(attacker.final_attack() * (1 - self.final_protection()), 1)
            )
        self.hp = self.hp - damage
        messages.defend_action_arena(attacker, self, damage)


class Paladin(Person):
    def __init__(self, name, hp, base_ad, base_resist):
        self.name = name
        self.hp = hp * 1.5
        self.base_ad = base_ad
        self.max_hp = self.hp
        self.base_resist = base_resist * 2
        self.items = []


class Warrior(Person):
    def __init__(self, name, hp, base_ad, base_resist):
        self.name = name
        self.hp = hp
        self.base_ad = base_ad * 2
        self.max_hp = hp
        self.base_resist = base_resist
        self.items = []
