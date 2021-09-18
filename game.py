from colorama import Fore, Back, Style
from colorama import init
import operator
import random

init()

NAMES = ['Антон', 'Павел', 'Сэм', 'Люси', 'Брэйн', 'Ричард', 'Софи', 'Грэг', 'Джон',
    'Тревор', 'Пикачу', 'Бульбазавр', 'Чермандер', 'Сквиртл', 'Баттерфри', 'Пиджи',
    'Спироу', 'Глум', 'Вульпикс', 'Парас',
]

class Thing():
    """Создаем модель вещи для персонажа."""
    def __init__(self, name, protection_level, attack, life):
        self.name = name
        self.protection_level = protection_level
        self.attack = attack
        self.life = life


class Person():
    """Создаем модель персонажа."""
    def __init__(self, name, protection_level, attack, life):
        self.name = name
        self.protection_level = protection_level
        self.attack = attack
        self.life = life
    
    def set_things(self, things):
        for thing in things:
            self.protection_level = thing.protection_level + self.protection_level
            self.attack = thing.attack + self.attack
            self.life = thing.life + self.life
    
    def lose_life(self, attack_damage):
        self.life = self.life - (attack_damage - attack_damage*self.protection_level)

    
class Paladin(Person):
    """Представляет аспекты персонажа, специфические для Паладина."""
    def __init__(self, name, protection_level, attack, life):
        super().__init__(name, protection_level, attack, life)
        self.protection_level = self.protection_level * 2
        self.life = self.life * 2


class Warrior(Person):
    """Представляет аспекты персонажа, специфические для Воина."""
    def __init__(self, name, protection_level, attack, life):
        super().__init__(name, protection_level, attack, life)
        self.attack = self.attack * 2


def random_params():
    name = random.choice(NAMES)
    protection_level = random.uniform(0, 0.1) 
    attack = random.randint(5, 100)
    life = random.randint(50, 500)
    params = {'name': name, 'protection_level': protection_level, 'attack': attack, 'life': life}
    return params

def create_personages():
    paladins = []
    warriors = []
    persons = []
    value = 0
    number_of_paladins = random.randint(0, 5)
    number_of_warriors = random.randint(0, 5)
    number_of_persons = 10 - number_of_paladins - number_of_warriors
    while value != number_of_paladins:
        paladin = Paladin(
            random_params()['name'],
            random_params()['protection_level'],
            random_params()['attack'],
            random_params()['life']
        )
        paladins.append(paladin)
        value = value + 1
        print(f'На арену выходит паладин {paladin.name}')
    value = 0
    while value != number_of_warriors:
        warrior = Warrior(
            random_params()['name'],
            random_params()['protection_level'],
            random_params()['attack'],
            random_params()['life']
        )
        warriors.append(warrior)
        value = value + 1
        print(f'На арену выходит воин {warrior.name}')
    value = 0
    while value != number_of_persons:
        person = Person(
            random_params()['name'],
            random_params()['protection_level'],
            random_params()['attack'],
            random_params()['life']
        )
        persons.append(person)
        value = value + 1
        print(f'На арену выходит {person.name}')
    personages = paladins + warriors + persons
    return personages

knife = Thing('нож', 0, 10, 0)
pitchfork = Thing('вилы', 0, 5, 0)
sword = Thing('меч', 0, 25, 0)
armour = Thing('броня', 0.1, 0, 0)
magic_ring = Thing('магическое кольцо', 0.01, 0, 15)
shield = Thing('щит', 0.05, 1, 0)

def things_choice():
    ammunition = [knife, pitchfork, sword, armour, magic_ring, shield]
    things = []
    number_of_things = random.randint(0, 4)
    value = 0
    while value != number_of_things:
        thing = random.choice(ammunition)
        things.append(thing)
        value = value + 1
    things = sorted(things, key=operator.attrgetter('protection_level'))
    return things

def fight():
    personages = create_personages()
    for personage in personages:
        things = things_choice()
        personage.set_things(things)
    while len(personages) != 1:
        attacker = random.choice(personages)
        defender = random.choice(personages)
        attack_damage = attacker.attack
        finalProtection = defender.protection_level
        defender.lose_life(attack_damage)
        damage = int(attack_damage - attack_damage*finalProtection)
        print(f'{attacker.name.title()} наносит удар по {defender.name.title()} на {damage} урона')
        if defender.life <= 0:
            print(Fore.RED + f'{defender.name} храбро сражался, но был повержен.' + Style.RESET_ALL)
            personages.remove(defender)
    print(Fore.BLACK + Back.WHITE + f'В тяжелейшей схватке победил {personages[0].name}' + Style.RESET_ALL)

fight()