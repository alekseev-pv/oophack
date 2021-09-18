import colorama
import random

from data import PERSONS, THINGS
from colorama import Fore

colorama.init()


class Base:
    def __init__(self, name, hp, attack, protection):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.protection = protection


class Thing(Base):
    pass


class Person(Base):
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack, protection)
        self.things = []
        self.final_hp = self.hp + sum(thing.hp for thing in self.things)
        self.final_protection = self.protection + sum(thing.protection for thing in self.things)
        self.attack_damage = self.attack + sum(thing.attack for thing in self.things)

    def set_things(self, things):
        self.things.extend(things)

    def hit_points(self, other):
        print(Fore.RED + f'{other.name} наносит удар {self.name} на {other.attack_damage} очков урона')
        hp = self.final_hp - (other.attack_damage - other.attack_damage * self.final_protection * 0.01)
        self.final_hp = hp
        print(Fore.GREEN + f'   Уровень жизни {self.name}: {hp}')
        return hp


class Paladin(Person):
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, 2 * hp, attack, 2 * protection)


class Warrior(Person):
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, 2 * attack, protection)


def main():
    things = []
    for thing in THINGS:
        things.append(Thing(**thing))

    persons = []
    count_of_paladins = random.randint(1, 10)
    paladins = random.sample(PERSONS, count_of_paladins)
    count_of_warriors = 10 - count_of_paladins
    for person in PERSONS:
        if person in paladins:
            PERSONS.remove(person)
    warriors = random.sample(PERSONS, count_of_warriors)
    for paladin in paladins:
        persons.append(Paladin(**paladin))
    for warrior in warriors:
        persons.append(Warrior(**warrior))

    for person in persons:
        count_of_things = random.randint(1, 4)
        person.set_things(random.sample(things, count_of_things))

    print(Fore.YELLOW + '   ДА НАЧНЕТСЯ БИТВА!')
    print()
    while len(persons) > 1:
        fighters = random.sample(persons, 2)
        print(Fore.CYAN + f'На арену выходят {fighters[0].name} и {fighters[1].name}')
        while True:
            first = fighters[0].hit_points(fighters[1])
            if first <= 0:
                print(Fore.WHITE + f'{fighters[0].name} проиграл :(')
                persons.remove(fighters[0])
                break

            second = fighters[1].hit_points(fighters[0])

            if second <= 0:
                print(Fore.WHITE + f'{fighters[1].name} проиграл :(')
                persons.remove(fighters[1])
                break
        print()

    print(Fore.MAGENTA + f'{persons[0].name} победил!')


if __name__ == "__main__":
    main()
