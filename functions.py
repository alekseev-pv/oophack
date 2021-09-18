import random
from colorama import Fore, Back, Style
from names_library import CLASS, NAME, SURNAME
from thing_library import THING_LIBRARY


def create_table(number: int = 4):
    fighters_list = []
    for _ in range(1, number + 1):
        spot = []
        for _ in range(1, 3):
            name = NAME[random.randint(1, len(NAME.keys()))]
            surname = SURNAME[random.randint(1, len(SURNAME.keys()))]
            full_name = name + ' ' + surname
            fighter_class = CLASS[random.randint(1, len(CLASS.keys()))]
            fighter_inventory = []
            for _ in range(5):
                chance = random.randint(1, 100)
                if chance >= 75:
                    thing = THING_LIBRARY[random.randint(1, len(THING_LIBRARY.keys()))]
                    fighter_inventory.append(thing)
            spot.append(fighter_class(full_name, fighter_inventory))
        fighters_list.append(spot)
    return fighters_list


def fight_table(fighters_list):
    new_fighter_list_1 = []
    for fighter_spot in fighters_list:
        winner = fight_spot(fighter_spot)
        new_fighter_list_1.append(winner)
    if len(new_fighter_list_1) > 2:
        print(Fore.LIGHTBLUE_EX + 'Следующий раунд!')
        next_round = new_table(new_fighter_list_1)
        fight_table(next_round)
    else:
        print(Fore.CYAN + 'Последний бой!')
        fighter_1 = new_fighter_list_1[0]
        fighter_2 = new_fighter_list_1[1]
        print(Fore.LIGHTYELLOW_EX + f'В бой вступают: {fighter_1.name_class} {fighter_1.name} '
                                    f'и {fighter_2.name_class} {fighter_2.name}')
        while (fighter_1.health > 0) and (fighter_2.health > 0):
            print(Fore.RED + f'{fighter_1.name} наносит удар')
            fighter_2.hit(fighter_1.damage)
            if fighter_2.health > 0:
                print(Fore.RED + f'{fighter_2.name} наносит удар')
                fighter_1.hit(fighter_2.damage)
        if fighter_1.health > 0:
            print(Fore.YELLOW + f'{fighter_1.name_class} {fighter_1.name} - Герой Арены!')
            return fighter_1
        if fighter_2.health > 0:
            print(Fore.YELLOW + f'{fighter_2.name_class} {fighter_2.name} - Герой Арены!')
            return fighter_2


def fight_spot(fighter_spot: list):
    fighter_1 = fighter_spot[0]
    fighter_2 = fighter_spot[1]
    print(Fore.LIGHTYELLOW_EX + f'В бой вступают: {fighter_1.name_class} {fighter_1.name} '
          f'и {fighter_2.name_class} {fighter_2.name}')
    while (fighter_1.health > 0) and (fighter_2.health > 0):
        print(Fore.RED + f'{fighter_1.name} наносит удар')
        fighter_2.hit(fighter_1.damage)
        if fighter_2.health > 0:
            print(Fore.RED + f'{fighter_2.name} наносит удар')
            fighter_1.hit(fighter_2.damage)
    if fighter_1.health > 0:
        print(Fore.LIGHTGREEN_EX + f'{fighter_1.name_class} {fighter_1.name} победил в схватке')
        return fighter_1
    if fighter_2.health > 0:
        print(Fore.LIGHTGREEN_EX + f'{fighter_2.name_class} {fighter_2.name} победил в схватке')
        return fighter_2


def new_table(lst):
    new_list = []
    for i in range(len(lst)):
        if i % 2 == 0:
            var = lst[i:i + 2]
            # print(var)
            new_list.append(var)
    return new_list


def start():
    table = create_table(4)
    fight_table(table)


if __name__ == '__main__':
    start()
