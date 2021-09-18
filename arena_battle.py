import random

from colorama import Fore, init

from classes import Paladin, Warrior
from items import Thing

init(autoreset=True)
HERO_NAMES = [
    Fore.RESET + 'Геральт',
    Fore.RESET + 'Майкл Джексон',
    Fore.RESET + 'Бобби',
    Fore.RESET + 'Читер',
    Fore.RESET + 'Твой сосед',
    Fore.RESET + 'Вордт из холодной долины',
    Fore.RESET + 'Майор Pain',
    Fore.RESET + 'Игрок старкрафт',
    Fore.GREEN + 'Erduyta',
    Fore.LIGHTMAGENTA_EX + 'Aalechkaa',
    Fore.RESET + 'Игрок Genshin',
    Fore.RESET + 'Бобби',
    Fore.RESET + 'Dude',
    Fore.RESET + 'Чеееел',
    Fore.RESET + 'Учитель',
    Fore.RESET + 'Терминатор',
    Fore.RESET + 'Волшебник страны Оз'
]


class Arena:
    def __init__(self) -> None:
        self.participants = []
        self.generate_heroes()
        self.assign_items()
        self.play()

    def generate_heroes(self):
        available_names = HERO_NAMES
        for i in range(10):
            name = random.choice(available_names)
            available_names.remove(name)
            protection = random.randint(9, 11)
            attack = random.randint(9, 11)
            health = 30 - attack - protection
            random_class = random.randint(0, 1)
            if random_class == 0:
                participant = Paladin(name, health, attack/2, protection/40)
            if random_class == 1:
                participant = Warrior(name, health, attack/2, protection/40)
            self.participants.append(participant)

    def generate_item(self) -> Thing:
        name = 'Магическое кольцо участника арены'
        protection = random.randint(5, 10)
        attack = random.randint(5, 10)
        health = 0  # random.randint(-5, 20)
        return Thing(name, protection/100, attack/10, health/10)

    def assign_items(self):
        for hero in self.participants:
            count = random.randint(1, 4)
            items_to_equip = []
            for i in range(count):
                items_to_equip.append(self.generate_item())
            hero.set_things(items_to_equip)

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
                print(f'{defender.name} ' + Fore.RESET + 'погибает!')
