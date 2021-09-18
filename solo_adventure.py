import random

from colorama import Fore, init

import messages
from classes import Paladin, Person, Warrior

init(autoreset=True)


class Adventure:
    def __init__(self, chosen_class) -> None:
        protection = random.randint(9, 11)
        attack = random.randint(9, 11)
        health = 30 - attack - protection
        name = messages.solo_name()
        if chosen_class == 'paladin':
            self.hero = Paladin(name, health, attack/2, protection/40)
        if chosen_class == 'warrior':
            self.hero = Warrior(name, health, attack/2, protection/40)
        self.child_dream = False
        self.elder = False
        self.elder2 = False
        self.witch = False
        self.start()

    def start(self):
        messages.solo_start(self)


class SoloBattle:
    def __init__(self, adventure: Adventure, enemy: Person) -> None:
        self.participants = []
        self.participants.append(adventure.hero)
        self.participants.append(enemy)
        self.hero = adventure.hero
        self.if_win = False
        self.play()

    def play(self):
        heroes = []
        for hero in self.participants:
            heroes.append(hero.name)
        strng_of_heroes = ', '.join(heroes)
        print(f'На арену входят: {strng_of_heroes}')
        while len(self.participants) > 1:
            defender = random.choice(self.participants)
            self.participants.remove(defender)
            attacker = random.choice(self.participants)
            defender.defend(attacker)
            if defender.hp > 0:
                self.participants.append(defender)
            else:
                print(f'{defender.name}' + Fore.RESET + ' погибает!')
        if self.participants[0] == self.hero:
            self.if_win = True
