from os import name
from time import sleep
from typing import Dict
from classes import Paladin, Shaman
from characters import Person
from random import sample, shuffle, randint, choices
import inspect

ALLINSE = (Paladin,)
HORDE = (Shaman,)
MAX_ITEMS = 4


def fight(player_1: Person, player_2: Person, rounds: int = 1):
    ''' Возвращает того, что умер '''
    # Кто атакует первый?
    all_fights = []
    for _ in range(rounds):
        one_attacks_two = (player_1, player_2)
        two_attacks_one = (player_2, player_1)
        fights = [one_attacks_two, two_attacks_one]
        shuffle(fights)
        all_fights.append(fights[0])
    # print(all_fights)


    for count, pair in enumerate(all_fights, start=1):
        print(f'ROUND {count}! FIGHT!')
        #print(pair)
        attacker, victim = pair
        #print(attacker)
        while True:
            attacker.attack(victim)
            print()
            #sleep(5)
            if victim.hp <= 0:
                print(f'{attacker} WINS!')
                return victim

            victim.attack(attacker)
            #sleep(5)
            print()

            if attacker.hp <= 0:
                print(f'{victim} WINS!')
                return attacker
            #sleep(1)

def take_on_gear(player, gears_dict):
    count = 0
    # Тип обязательные реликвии, дял фаркций
    for i in ALLINSE:
        if isinstance(player, i):
            print('\nЭкипировка фракционных айтемов!')
            #sleep(1)
            print(player.take_on_cheracter_gear(gears_dict["alliance_items"]))
            count += 1
            break
    for i in HORDE:
        if isinstance(player, i):
            print('\nЭкипировка фракционных айтемов!')
            #sleep(1)
            print(player.take_on_cheracter_gear(gears_dict["horde_items"]))
            count += 1
            break
    print('Выдаем рандомное снаряжение!\n')
    need_items = randint(1, MAX_ITEMS-count)
    # print(need_items)
    # Выбираем рандомный гир (уникальный)
    rand_gear = sample(gears_dict['any_items'], k=need_items)
    print(player.take_on_cheracter_gear(rand_gear))

def choice_class(person: Person, needed_class):
    return needed_class(
        name = person.name,
        hp = person.hp,
        base_damage=person.damage,
        base_protection=person.protection
    )
# def pars_players(players:Dict) -> Dict:
#     players_dict={}
#     for player, stats in players.items():
#         try:
#             players_dict[player]
#         except KeyError:
#             players_dict[player] = []
#         name, hp, base_attack, base_protection = stats.values()

