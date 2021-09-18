from os import name
from classes import Paladin, Shaman
from characters import Person
from random import shuffle, randint, choices
import inspect

ALLINSE = (Paladin,)
HORDE = (Shaman,)
MAX_ITEMS = 4


def fight(player_1: Person, player_2: Person, rounds: int = 1):
    
    # Кто атакует первый?
    all_fights = []
    for _ in range(rounds):
        one_attacks_two = (player_1, player_2)
        two_attacks_one = (player_2, player_1)
        fights = [one_attacks_two, two_attacks_one]
        shuffle(fights)
        all_fights.append(fights[0])
    print(all_fights)


    for count, pair in enumerate(all_fights, start=1):
        print(f'ROUND {count}! FIGHT!')
        #print(pair)
        attacker, victim = pair
        print(attacker)
        while True:
            attacker.attack(victim)
            print()
            if victim.hp <= 0:
                print(f'{attacker} WINS!')
                break

            victim.attack(attacker)
            print()

            if attacker.hp <= 0:
                print(f'{victim} WINS!')
                break

def take_on_gear(player, gears_dict):
    count = 0
    # Тип обязательные реликвии, дял фаркций
    for i in ALLINSE:
        if isinstance(player, i):
            print('Экипировка фракционных айтемов!')
            print(player.take_on_cheracter_gear(gears_dict["alliance_items"]))
            count += 1
    for i in HORDE:
        if isinstance(player, i):
            print('Экипировка фракционных айтемов!')
            print(player.take_on_cheracter_gear(gears_dict["horde_items"]))
            count += 1
    print('Выдаем рандомное снаряжение!\n')
    need_items = randint(1, MAX_ITEMS-count)
    # Выбираем рандомный гир
    rand_gear = choices(gears_dict['any_items'], k=need_items)
    print(player.take_on_cheracter_gear(rand_gear))

def choice_class(person: Person, needed_class):
    return needed_class(
        name = person.name,
        hp = person.hp,
        base_atack=person.atack,
        base_protection=person.protection
    )