from random import choice
from typing import List
import math

from colorama import Fore, Back, Style

from person import Person


# def simple_distance(attacker, target):
#     distance = math.sqrt(((attacker.point[0] - target.point[0]) ** 2) + ((attacker.point[1] - target.point[1]) ** 2))
#     return round(distance, 2)


def start_fight(percs):
    attack_pers = None
    while len(percs) > 1:
        attack_pers = choice(percs)
        defend_pers = choice(percs)
        while attack_pers == defend_pers:
            defend_pers = choice(percs)
        print(attack_pers.simple_distance(defend_pers))
        print(f'Радиус {attack_pers.radius_attack}')
        if attack_pers.simple_distance(defend_pers) <= attack_pers.radius_attack:
            stat_battle = defend_pers.under_attack(attack_pers)
            print(Back.RED + Fore.BLACK +
                  f'Атакует: {attack_pers.name}, '
                  f'сила атаки: {stat_battle["attack_power"]}' + Style.RESET_ALL)
            print(Back.CYAN + Fore.BLACK +
                  f'Защищается: {defend_pers.name}' +
                  f' здоровья после атаки: {stat_battle["hp_after_attack"]}'
                  + Style.RESET_ALL)
        else:
            attack_pers.run_to_target(defend_pers)
            print(Back.YELLOW + Fore.BLACK +
                  f'Атакующий: {attack_pers.name}, '
                  f'бежит к цели: {defend_pers.name}' + Style.RESET_ALL)
        if defend_pers.final_hp == 0:
            percs.remove(defend_pers)
    print('\n')
    print(Back.YELLOW + Fore.BLACK + f'Бой закончен! Победитель {attack_pers.name}!' + Style.RESET_ALL)

# def find_nearest_for_attack(attacker: Person, others: List[Person]):
#     nearest_space = 0
#     for victim in others:
#         if abs(attacker.point[0] - victim.point[0]) <= attacker.radius_attack:
#             return victim
#         else:
#             a_x =
#             distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
