from random import randint, choice, sample
import json
import time


class PropertyGenerator:
    """This class generate names of artefacts."""
    NAMES_THINGS_DEFAULT = ["Hatred's Grimoire",
                            "Heavenly Disc",
                            "Divine Scroll",
                            "Invisible Horn",
                            "Scourge Cloak",
                            "Mirror of Service",
                            "Circlet of All-Seeing",
                            "Grail of Angels",
                            "Staff of the Occult",
                            "Cylinder of the Creed"]
    NAMES_PERSON_DEFAULT = ["Harry Potter",
                            "Spider Man",
                            "Batman",
                            "Optimus Praim",
                            "Iron Man",
                            "Arthas Menethil",
                            "Sarah Louise Kerrigan",
                            "James Eugene Raynor",
                            "Декард Каин",
                            "Синдзи Икари"]

    @classmethod
    def _get_things_names(cls):
        try:
            with open(file="things_names.json", mode="r") as file:
                things_names = json.load(file)
                return list(things_names.keys())
        except FileNotFoundError:
            return PropertyGenerator.NAMES_THINGS_DEFAULT

    @classmethod
    def _get_persons_names(cls):
        try:
            with open(file="persons_names.json", mode="r", encoding="utf-8") as file:
                persons_names = json.load(file)
                return list(persons_names)
        except FileNotFoundError:
            return PropertyGenerator.NAMES_PERSON_DEFAULT


    @classmethod
    def give_name(cls, type_name="things"):
        if type_name == "things":
            names = PropertyGenerator._get_things_names()
        elif type_name == "persons":
            names = PropertyGenerator._get_persons_names()
        else:
            raise ValueError("Такого типа имён не существует.")
        return choice(names)


class Thing:
    """This class """

    def __init__(self):
        self.name = PropertyGenerator.give_name()
        self.attack = randint(0, 10)
        self.health = randint(0, 100)
        self.protect = randint(0, 10)

    def __str__(self):
        return (f"У вас в руках {self.name}\n"
                f"Ваши бонусы: "
                f"{self.attack} к атаке,"
                f"{self.health} к здоровью,"
                f"{self.protect} к защите.")

    @classmethod
    def generate_things(cls, quantity: int = 1):
        # TODO доавить проверку уникальности предмета
        things = [Thing() for _ in range(quantity)]
        things.sort(key=lambda obj: obj.protect)
        return things


class Person:
    """Class of game characters."""

    def __init__(self, name: str = "Harry",
                 attack: int = 5, health: int = 50, protect: int = 0):
        self.name = PropertyGenerator.give_name(type_name="persons")
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

    def is_alive(self):
        return self.health > 0

    def get_things(self, things: list) -> None:
        self.things = things
        self.__update_parameters()

    def take_damage(self, attack_hero: object):
        attack_damage = attack_hero.full_attack
        self.full_health - attack_damage * (1 - self.full_protect)
        print(f"{attack_hero.name} наносит удар по "
              f"{self.name} на {attack_damage} урона")

    def __str__(self):
        return self.name


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.protect *= 2


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.attack *= 2


class Tank(Person):
    def __init__(self):
        super().__init__()
        self.health *= 2


class Battle:
    HEROS_TYPES = [Paladin, Warrior, Tank]
    PRINT_PAUSE = 0.01
    PRINT_PAUSE_HERO = 0.5

    def __init__(self, count_heroes:int =2):
        self.count_heroes =count_heroes # TODO добавить валидацию
        self.cunt_heroes = count_heroes
        self.heroes = []
        self.things = []

    def _beauti_line_print(self):
        for _ in range(100):
            print("-", end="")
            time.sleep(Battle.PRINT_PAUSE)
        print()

    def heroes_print(self):
        for hero in self.heroes:
            print(f"{hero.name:^100}")
            time.sleep(Battle.PRINT_PAUSE_HERO)

    def print_heroes_artefacts(self):
        for hero in self.heroes:
            hero_things = ", ".join([thing.name for thing in hero.things])
            print(f"{hero.name}: {hero_things}")
            time.sleep(Battle.PRINT_PAUSE_HERO)

    def get_fighters(self):
        first = self.heroes.pop(randint(0, len(self.heroes)))
        second = self.heroes.pop(randint(0, len(self.heroes)))
        return [first, second]

    def add_things(self):
        """Добавляем вещи"""
        self.things = Thing.generate_things(randint(10, 50))

    def add_heroes(self):
        """Создаём героев."""
        for _ in range(self.count_heroes):
            hero_class = choice(Battle.HEROS_TYPES)
            self.heroes.append(hero_class())

    def give_things_to_heroes(self):
        """Раздаём героям вещи"""
        [hero.get_things(sample(self.things, randint(1,4)))
         for hero in self.heroes]

    def fight(self, fighters, count):
        first_hero, second_hero = fighters
        print(f"В бою № {count} сойдутся {first_hero} и {second_hero}.")
        while True:
            first_attack_hero = fighters.pop(randint(0, 1))
            second_attack_hero = fighters[0]
            second_attack_hero.take_damage(first_attack_hero)
            if not second_attack_hero.is_alive:
                break
            first_attack_hero.take_damage(second_attack_hero)
            if not first_attack_hero.is_alive:
                break
            winner = first_hero if first_hero.is_alive else second_hero
            print(f"В этом бою победил {winner.name}")




    def battle_prepare(self):
        self.add_heroes()
        self.add_things()
        self.give_things_to_heroes()

    def battle_intro(self):
        self.battle_prepare()
        print("Давным давно.")
        time.sleep(1)
        print("В не очень далёкой галактике!")
        time.sleep(1)
        self._beauti_line_print()
        print(f"{'Сошлись в поединке:':^100}")
        self._beauti_line_print()
        self.heroes_print()
        self._beauti_line_print()
        print(f"{'У каждого был при себе артефакт невиданной мощи!':^100}")
        self._beauti_line_print()
        self.print_heroes_artefacts()
        self._beauti_line_print()

    def start_battle(self):
        print(f"{'Битва началась':^100}")
        self._beauti_line_print()
        self.next_round = []
        count = 1
        while len(self.heroes) > 1:
            fighters = self.get_fighters()
            self.fight(fighters, count)




if __name__ == "__main__":
    battle = Battle(count_heroes=10)
    battle.battle_intro()
    battle.start_battle()





