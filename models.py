import random
import json


class PropertyGenerator:
    """This class generate names of artefacts."""
    NAMES_DEFAULT = ["Hatred's Grimoire",
                     "Heavenly Disc",
                     "Divine Scroll",
                     "Invisible Horn",
                     "Scourge Cloak",
                     "Mirror of Service",
                     "Circlet of All-Seeing",
                     "Grail of Angels",
                     "Staff of the Occult",
                     "Cylinder of the Creed"]

    @classmethod
    def _get_things_names(cls):
        try:
            with open(file="things_name1.json", mode="r") as file:
                things_names = json.load(file)
                return list(things_names.keys())
        except FileNotFoundError:
            return PropertyGenerator.NAMES_DEFAULT

    @classmethod
    def give_name(cls):
        names = PropertyGenerator._get_things_names()
        return random.choice(names)


class Thing:
    """This class """

    def __init__(self):
        self.name = PropertyGenerator.give_name()
        self.attack = random.randint(0, 10)
        self.health = random.randint(0, 100)
        self.protect = random.randint(0, 30)

    def __str__(self):
        return (f"У вас в руках {self.name}\n"
                f"Ваши бонусы: "
                f"{self.attack} к атаке,"
                f"{self.health} к здоровью,"
                f"{self.protect} к защите.")

    def __repr__(self):
        return str(self.protect)

    @classmethod
    def generate_things(cls, quantity: int = 1):
        # TODO доавить проверку уникальности предмета
        things = [Thing() for _ in range(quantity)]
        things.sort(key=lambda obj: obj.protect)
        return things

things = Thing.generate_things(4)
print(things)

class Person:
    """Class of game characters."""

    def __init__(self, name: str = "Harry",
                 attack: int = 5, health: int = 50, protect: int = 0):
        self.name = name
        self.attack = attack
        self.health = health
        self.protect = protect
        self.things = []

    def __update_parameters(self) -> None:
        self.full_attack = (self.attack +
                            sum(thing.__dict__["attack"] for thing in self.things))
        self.full_health = (self.health +
                            sum(thing.__dict__["health"] for thing in self.things))
        self.full_protect = (self.protect +
                             sum(thing.__dict__["protect"] for thing in self.things))

    def is_hero_alive(self):
        return self.health == 0

    def get_things(self, things: list) -> None:
        self.things = things
        self.__update_parameters()

    def take_damage(self, attack_hero: object):
        attack_damage = attack_hero.full_attack
        self.full_health - attack_damage * (1 - self.full_protect)
        print(f"{attack_hero.name} наносит удар по "
              f"{self.name} на {attack_damage} урона")


class Paladin(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.protect *= 2


class Warrior(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.attack *= 2


class Monk(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.health *= 2

