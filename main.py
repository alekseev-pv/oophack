"""OOP Game"""

import time
from random import choice, randint
from typing import List, Optional
from progress.bar import Bar

from colorama import init, Fore, Back, Style

NAMES = [
    'Fedya',
    'Vitya',
    'Gosha',
    'DarkLord',
    'Noname',
    'Frodo',
    'Felix',
    'John',
    'Geralt',
    'Aska',
    'Rei',
    'Eva',
    'Legoman',
    'BlackWitch',
    'Batman',
    'UntitledGoose',
    'UnbeatableRat',
    'Gollum',
    'Futaba',
    'Nioh',
]


class Thing:
    def __init__(self,
                 name: str,
                 defense_rate: float = 0,
                 attack_rate: float = 0,
                 hp_plus: float = 0) -> None:
        self.name = name
        self.defense_rate = defense_rate
        self.attack_rate = attack_rate
        self.hp_plus = hp_plus
        assert defense_rate <= 0.1, 'defense rate cannot be more than 0.1'

    def __str__(self):
        return (f"It's {self.name}, gives:\n"
                f"defense rate={self.defense_rate},\n"
                f"attack rate={self.attack_rate},\n"
                f"hp plus={self.hp_plus}.")


class Person:
    def __init__(self,
                 name: str,
                 start_hp: float = 100,
                 attack: float = 12,
                 defense: float = 0.1) -> None:
        self.name = name
        self.start_hp = start_hp
        self.attack = attack
        self.defense = defense
        self.things: List = []
        self.taked_dmg = 0

    def __str__(self) -> str:
        return (f'Name is {self.name}, hp={self.start_hp}, '
                f'attack={self.attack}, defense={self.defense}')

    def set_things(self, thing) -> None:
        self.things.append(thing)

    def check_protection(self) -> float:
        protection_bonus = float(0)
        for i in self.things:
            if i.defense_rate != 0:
                protection_bonus += i.defense_rate
        return self.defense + protection_bonus

    def taking_damage(self, damage: float) -> None:
        self.taked_dmg += damage - (damage * self.check_protection())

    def check_hp(self) -> float:
        hp_bonus = float(0)
        for i in self.things:
            if i.hp_plus != 0:
                hp_bonus += i.hp_plus
            result = self.start_hp + hp_bonus - self.taked_dmg
            if result < 0:
                return 0
        return result

    def check_dmg(self) -> float:
        attack_bonus = float(0)
        for i in self.things:
            if i.attack_rate != 0:
                attack_bonus += i.attack_rate
        return self.attack + (self.attack * attack_bonus)


class Warrior(Person):
    def __init__(self,
                 name: str,
                 start_hp: float = 100,
                 attack: float = 12,
                 defense: float = 0.1) -> None:
        super().__init__(name, start_hp, attack, defense)
        self.attack = attack * 2


class Paladin(Person):
    def __init__(self,
                 name: str,
                 start_hp: float = 100,
                 attack: float = 12,
                 defense: float = 0.1) -> None:
        super().__init__(name, start_hp, attack, defense)
        self.start_hp = start_hp * 2
        self.defense = defense * 2


persons = []


def make_worriors():
    person1 = Warrior(name=choice(NAMES))
    person2 = Warrior(name=choice(NAMES))
    person3 = Warrior(name=choice(NAMES))
    person4 = Warrior(name=choice(NAMES))
    person5 = Warrior(name=choice(NAMES))
    person6 = Paladin(name=choice(NAMES))
    person7 = Paladin(name=choice(NAMES))
    person8 = Paladin(name=choice(NAMES))
    person9 = Paladin(name=choice(NAMES))
    person10 = Paladin(name=choice(NAMES))

    persons = [
        person1,
        person2,
        person3,
        person4,
        person5,
        person6,
        person7,
        person8,
        person9,
        person10,
    ]

    persons = set_count_of_worriors(persons)

    for i in persons:
        persons_names = []
        while i.name in persons_names:
            i.name = choice(NAMES)
        persons_names.append(i.name)
    return persons


def make_things_and_give_to_worriors():
    sword = Thing('sword', attack_rate=0.3)
    axe = Thing('axe', attack_rate=0.2)
    magic_staff = Thing('magic_staff', attack_rate=0.3, hp_plus=20)
    keysword = Thing('keysword', attack_rate=0.4, hp_plus=30)
    mastersword = Thing('mastersword', attack_rate=0.5, hp_plus=10)
    peak = Thing('peak', attack_rate=0.2)
    shield = Thing('shield', defense_rate=0.1)
    magick_shield = Thing('magick_shield', defense_rate=0.1, hp_plus=20)

    things = [
        sword, axe, magic_staff, keysword, mastersword, peak, shield, magick_shield
    ]

    def sort_key(s):
        return s.defense_rate

    things = sorted(things, key=sort_key)

    for i in persons:
        for a in range(0, randint(1, 4)):
            i.set_things(choice(things))


def set_count_of_worriors(pers):
    number = 0
    while True:
        number = int(input('Enter count of worriors in battle from 2 to 10\n'))
        if number >= 2 and number <= 10:
            break
        else:
            print('Not right number')
    if number == 10:
        return pers
    n = 10 - number
    for i in range(10 - number):
        pers.pop(-1)
    return pers


def fight(fighters_list):
    attaker = choice(fighters_list)
    defender = choice(fighters_list)
    while attaker.name == defender.name:
        defender = choice(fighters_list)
    print(Fore.YELLOW +
          f'Death fight betwen {attaker.name} and {defender.name}!\n')
    print(Fore.BLUE + f'Stats of battle:\n')
    print(attaker.name)
    print(f'hp={attaker.check_hp()}')
    print(f'defense rate={attaker.check_protection()}')
    print(f'power={attaker.check_dmg()}\n')
    print(defender.name)
    print(f'hp={defender.check_hp()}')
    print(f'defense rate={defender.check_protection()}')
    print(f'power={defender.check_dmg()}\n' + Style.RESET_ALL)

    while True:
        bar = Bar('Battle progress: ', max = 5)
        for i in range(5):
            bar.next()
            time.sleep(0.5)
        bar.finish()
        print(f'{attaker.name} attaks {defender.name}!')
        defender.taking_damage(attaker.check_dmg())
        print(f'{defender.name} takes {attaker.check_dmg()} dammage')
        print(f'{defender.name}\'s hp is {defender.check_hp()} now\n')
        if defender.check_hp() <= 0:
            print(Fore.RED + f'{defender.name} is lose to {attaker.name}\n')
            return defender

        bar = Bar('Battle progress: ', max = 5)
        for i in range(5):
            bar.next()
            time.sleep(0.5)
        bar.finish()
        print(f'{defender.name} attaks {attaker.name}!')
        attaker.taking_damage(defender.check_dmg())
        print(f'{attaker.name} takes {defender.check_dmg()} dammage')
        print(f'{attaker.name}\'s hp is {attaker.check_hp()} now\n')
        if attaker.check_hp() <= 0:
            print(Fore.RED + f'{attaker.name} is lose to {defender.name}\n')
            return attaker


def arena(fighters):
    in_arena = fighters
    losers = []
    init()
    print(Fore.YELLOW + 'Start of epic batle of all times!!!\n')
    while len(in_arena) != 1:
        result = fight(in_arena)
        losers.append(result)
        in_arena.remove(result)
    print(Fore.YELLOW + f'The winner is {in_arena[0].name}\n')
    print(Fore.RED + 'losers:')
    for i in losers:
        print(i.name)


if __name__ == '__main__':
    persons = make_worriors()
    make_things_and_give_to_worriors()
    arena(persons)
