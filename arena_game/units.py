import random
from game_settings import *
import colorama


class Thing:

    def __init__(self, name=None, protection=None, attack=1, hp=1):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp

    def __lt__(self, other):
        return self.protection < other.protection

    def __repr__(self):
        return f'{self.name} {self.protection}'


class Person:
    """Основной класс персонажа в игре"""
    def __init__(self, name=None, hp=BASE_HP, protection=BASE_PROTECTION, attack=BASE_ATTACK):
        self.name = name
        self._hp = hp
        self._protection = protection
        self._attack = attack
        self.finalProtection = self._protection
        self.attack_damage = self._attack
        self.HitPoints = self._hp

    def set_things(self, things):
        if len(things) < MAX_THINGS_PER_PERSON:
            amount = random.randint(1, len(things))
        else:
            amount = random.randint(1, 4)
        things = sorted(random.sample(things, amount))

        self.finalProtection = self._protection + sum([thing.protection
                                                       for thing in things])
        self.attack_damage = self._attack + sum([thing.attack
                                                  for thing in things])
        self.HitPoints = self._hp + sum([thing.hp
                                         for thing in things])

    def __str__(self, color=colorama.Back.RESET):
        return f'{color}{self.name}{colorama.Back.RESET}'


class Paladin(Person):
    """Кастомный класс персонажа"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hp *= 2
        self._protection *= 2

    def __str__(self):
        return super().__str__(color=colorama.Back.WHITE)


class Warrior(Person):
    """Кастомный класс персонажа"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._attack *= 2

    def __str__(self):
        return super().__str__(color=colorama.Back.BLACK)


class Elf(Person):
    """Кастомный класс персонажа"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hp *= 4

    def __str__(self):
        return super().__str__(color=colorama.Back.MAGENTA)


# расы персонажей - создаем ссылки на классы из файла настроек
RACES = [eval(race) for race in GAME_RACES]


def select_race(name):
    return random.choice(RACES)(name)
