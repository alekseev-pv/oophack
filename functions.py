"""
Модуль в котором реализован алгоритм сценария игры.
"""
import random

from typing import List, Union, Tuple

from colorama import Back, Fore, Style

from models import Paladin, Thing, Warrior


CustomTuple = Tuple[List[Union[Paladin, Warrior]], List[Thing]]


def create_things(count_things: int = 20) -> List[Thing]:
    """
    Функция создания произвольного количества вещей (count_things).
    """
    data_of_things: List[Union[str, float]] = []
    list_of_things: List[Thing] = []
    with open("src/things.txt") as file:
        lines = file.readlines()[1:]
        for line in lines:
            thing: List[Union[str, float]]
            thing = line.strip().split(',')
            thing[1:] = map(float, thing[1:])
            data_of_things.append(thing)
    for num in range(count_things):
        thing = Thing(*random.choice(data_of_things))
        list_of_things.append(thing)

    list_of_things = sorted(list_of_things,
                            key=lambda thing: thing.protection)

    return list_of_things


def create_heroes() -> List[Union[Paladin, Warrior]]:
    """
    Функция создания 10 героев.
    """
    list_of_type_heroes: List[str] = ['Paladin', 'Warrior']
    list_of_heroes: List[Union[Paladin, Warrior]] = []

    with open("src/names.txt") as file:
        list_names = file.read().strip().split('\n')
    list_names = random.sample(list_names, 10)
    for iter in range(10):
        type_hero = random.choice(list_of_type_heroes)
        name = list_names[iter]
        hp = float(random.randrange(40, 100))
        protection = round(random.uniform(0, 0.1), 2)
        attack_damage = float(random.randrange(5, 20))
        hero: Union[Warrior, Paladin]
        if type_hero == 'Paladin':
            hero = Paladin(name, hp, protection, attack_damage)
        else:
            hero = Warrior(name, hp, protection, attack_damage)
        list_of_heroes.append(hero)
    return list_of_heroes


def dress_heroes(heroes: List[Union[Paladin, Warrior]],
                 list_of_things: List[Thing]) -> None:
    """
    Функция раздачи героям вещей/артефактов.
    """
    for hero in heroes:
        things = random.sample(list_of_things,
                               random.randrange(1, 5))
        hero.set_things(things)


def arena(heroes: List[Union[Paladin, Warrior]]) -> Union[Paladin, Warrior]:
    count_living_heroes = len(heroes)
    while count_living_heroes != 1:
        index_heroes = range(count_living_heroes)
        index_at_hero, index_def_hero = random.sample(index_heroes, 2)

        at_hero = heroes[index_at_hero]
        def_hero = heroes[index_def_hero]

        print(f"{at_hero.name}({at_hero.final_hp:.1f} hp) наносит удар по"
              f" {def_hero.name}({def_hero.final_hp:.1f} hp) на"
              f" {def_hero.damage_reduction(at_hero.final_attack_damage):.1f}"
              " урона")
        def_hero.taking_attack_damage(at_hero.final_attack_damage)
        if not def_hero.can_fight():
            print(Back.RED + Fore.WHITE + f"{def_hero.name} погиб!")
            del heroes[index_def_hero]
            print(Style.RESET_ALL)

        count_living_heroes = len(heroes)

    print(Back.WHITE + Fore.CYAN)
    print("Победитель")
    hero = heroes[0]
    hero.print_statistic()
    print(Style.RESET_ALL)

    return hero


def initial_heroes_and_things() -> CustomTuple:
    things = create_things()
    heroes = create_heroes()
    dress_heroes(heroes, things)
    return (heroes, things)
