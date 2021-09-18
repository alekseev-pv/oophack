from random import choice
from typing import List
import math
import curses

from colorama import Fore, Back, Style

from draw_fight_map import draw_all_percs
from person import Person


def find_nearest_for_attack(attacker: Person, all_fighters):
    def sort_key(s):
        return s[0]

    nearest_space = 0
    victims_distances = []
    for victim in all_fighters:
        if victim != attacker:
            distance = abs(attacker.simple_distance(victim))
            if distance <= attacker.radius_attack:
                return victim
            else:
                obj = [distance, victim]
                victims_distances.append(obj)
                if distance < nearest_space:
                    nearest_space = distance
    result = sorted(victims_distances, key=sort_key)[0][1]
    return result


def start_fight(percs):
    # TODO(view map of battle)
    attack_pers = None
    while len(percs) > 1:

        attack_pers = choice(percs)
        defend_pers = find_nearest_for_attack(attack_pers, percs)
        # print(attack_pers.simple_distance(defend_pers))
        # print(attack_pers.point)
        for item in attack_pers.point:
            if item > 100 or item < 0:
                print(f'ERROR {attack_pers}')
        for item in defend_pers.point:
            if item > 100 or item < 0:
                print(f'ERROR {defend_pers}')

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


def fight_with_map(percs, speed: float):
    attack_pers = None
    while len(percs) > 1:
        attack_pers = choice(percs)
        defend_pers = find_nearest_for_attack(attack_pers, percs)
        draw_all_percs(attack_pers, defend_pers, percs, speed)
        if attack_pers.simple_distance(defend_pers) <= attack_pers.radius_attack:
            defend_pers.under_attack(attack_pers)
        else:
            attack_pers.run_to_target(defend_pers)
        if defend_pers.final_hp == 0:
            percs.remove(defend_pers)
        draw_all_percs(attack_pers, defend_pers, percs, speed)
    print('\n')
    print(Back.YELLOW + Fore.BLACK + f'Бой закончен! Победитель {attack_pers.name}!' + Style.RESET_ALL)
