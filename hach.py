from typing import List
import random


class Thing:
    name: str
    defence: int
    attack: float
    hp: float
    is_weapon: bool
    is_clothes: bool

    def __init__(self, name, defence, attack, hp, is_weapon, is_clothes):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp
        self.is_weapon = is_weapon
        self.is_clothes = is_clothes


class Person:
    name: str
    defence: int
    final_defence: float
    hp: float
    attack_points: float
    things: List[Thing]

    def __init__(self, name, defence, attack_points, hp):
        self.name = name
        self.defence = defence
        self.attack_points = attack_points
        self.hp = hp

        self.final_defence_calc()

    def total_points(self, attrname):
        points = getattr(self, attrname)
        try:
            points += sum([getattr(thing, attrname) for thing in self.things])
        except AttributeError:
            pass

        return points

    def final_defence_calc(self):
        self.final_defence = self.total_defence() / 100

    def set_things(self, things):
        self.things = things
        self.final_defence_calc()

    def decrease_health_points(self, attack_damage):
        hp = self.hp - attack_damage * (
                    1 - self.final_defence)

        self.health_points = 0 if hp < 0 else hp

    def total_defence(self):
        return self.total_points('defence')

    def total_attack_points(self):
        return self.total_points('attack_points')

    def total_hp(self):
        return self.total_points('hp')

    def total_final_defence(self):
        return self.final_defence


class Paladin(Person):
    def __init__(self, name, defence, attack_points, hp):
        super().__init__(name, defence, attack_points, hp)

        self.hp *= 2
        self.defence *= 2


class Warrior(Person):
    def __init__(self, name, defence, attack_points, hp):
        super().__init__(name, defence, attack_points, hp)

        self.attack_points *= 2


class Game:
    things: List[Thing]

    def __init__(self, thing_settings, person_settings, things_pre_list):
        self.thing_settings = thing_settings
        self.person_settings = person_settings

        self.things = []
        self.create_things(things_pre_list)

    def create_things(self, things_pre_list):
        things_pre_list_count = len(things_pre_list)

        random.seed()
        things = []
        while len(things) < 5:
            tid = random.randint(0, things_pre_list_count - 1)
            pre_name, is_weapon, is_clothes, variants = things_pre_list[tid]

            name = pre_name + variants[random.randint(0, len(variants) - 1)]
            defence = random.randint(
                *self.thing_settings['Defence'])
            attack_points = random.randint(
                *self.thing_settings['AttackPoints'])
            hp = random.randint(
                *self.thing_settings['Hp'])

            things.append(
                Thing(
                    name=name,
                    defence=defence,
                    attack_points=attack_points,
                    hp=hp,
                    is_weapon=is_weapon,
                    is_clothes=is_clothes)
            )

        self.things = sorted(things, key=lambda v: v.defence)