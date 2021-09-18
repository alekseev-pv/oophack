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

    @classmethod
    def generate_things(cls, quantity: int = 1):
        # TODO доавить проверку уникальности предмета
        return [Thing() for _ in range(quantity)]

t = Thing()
print(t.__dict__)

class Person:
    PARAMETERS = ("attack", "health", "protect")

    def __init__(self, name: str = "Harry",
                 attack: int = 5, health: int = 50, protect: int = 0):
        self.name = name
        self.attack = attack
        self.health = health
        self.protect = protect
        self.things = []

    def _update_parameters(self):
        # TODO подумать о генерации новых параметров относительно исходных
        self.full_attack = self.attack + \
                            sum(thing.__dict__["attack"] for thing in self.things)
        self.full_health = self.health + \
                            sum(thing.__dict__["health"] for thing in self.things)
        self.full_protect = self.protect + \
                            sum(thing.__dict__["protect"] for thing in self.things)


    def get_things(self, things: list):
        self.things = things
        return self._update_parameters


