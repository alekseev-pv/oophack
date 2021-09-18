from random import shuffle, choice

from colorama import Fore, Style

from thing import Thing


def create_loot(lists_things):
    items = [Thing(name=name,
                   hp=hp,
                   attack_power=attack_power,
                   protection=protection)
             for name, hp, attack_power, protection in lists_things]
    print('-'*10)
    return items


def looting(lists_heroes, things):
    shuffle(lists_heroes)
    for hero in lists_heroes:
        if len(things) == 0:
            break
        else:
            hero.set_things(things)
            print('=' * 10)


def create_heroes(names_heroes, type_heroes, quantity_fighters):
    shuffle(names_heroes)
    print('-'*10)
    return [choice(type_heroes)(name=name)
            for name in names_heroes[:quantity_fighters]]


def battle(fights):

    for count, pair in enumerate(fights, start=1):
        print(Fore.RED + f'Раунд {count}! В бой!')
        print(Style.RESET_ALL)
        attacker, defender = pair
        attacker.attack(defender)
        print('=' * 10)
        if defender.current_health <= 0:
            print(Fore.RED + f'{defender} повержен, победил {attacker}!')
            print(Style.RESET_ALL)
            print('*' * 10)
            attacker.current_health = attacker.max_health
            return attacker
        defender.attack(attacker)
        print('=' * 10)
        if attacker.current_health <= 0:
            print(Fore.RED + f'{attacker} повержен, победил {defender}!')
            print(Style.RESET_ALL)
            print('*' * 10)
            defender.current_health = defender.max_health
            return defender


def start_of_battles(names_heroes,
                     type_heroes,
                     lists_things,
                     rounds,
                     quantity_fighters):
    things = create_loot(lists_things)
    heroes = create_heroes(names_heroes, type_heroes, quantity_fighters)
    looting(heroes, things)
    while len(heroes) != 1:
        shuffle(heroes)
        fighter_1 = heroes[0]
        fighter_2 = heroes[1]
        print(Fore.RED + f'{fighter_1} против {fighter_2}')
        print(Style.RESET_ALL)
        del heroes[0:2]
        first_fight_attack = (fighter_1, fighter_2)
        second_fight_attack = (fighter_2, fighter_1)
        fights = [first_fight_attack, second_fight_attack]
        shuffle(fights)
        all_fights = fights * rounds
        winner = battle(all_fights)
        heroes.append(winner)
    print('!'*10)
    print(Fore.RED + f'Бои окончены, победитель битвы {heroes[0]}!')
