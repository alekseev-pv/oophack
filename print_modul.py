
import os

from colorama import Fore, Style

from typing import List, Union

from models import Paladin, Thing, Warrior

from functions import arena


def clearConsole() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def enter_name() -> str:
    print()
    clearConsole()
    name = input(Fore.YELLOW + "Введите имя - ")
    clearConsole()
    width = os.get_terminal_size().columns
    print(f"Уважаемый {name}!".center(width))
    print("Приветствуем вас в игре ARENA".center(width))
    input("(Нажмите любую кнопку)".center(width))
    return name


def start_menu(name: str,
               num_arena: int,
               count_guess: int) -> int:
    width = os.get_terminal_size().columns

    clearConsole()

    print(Style.RESET_ALL)
    print(Fore.YELLOW + f"ARENA № {num_arena}".center(width))
    print("Выбери пункт из меню (введите номер пункта)".center(width))
    print("1. Посмотреть героев".center(width))
    print("2. Посмотреть артефакты".center(width))
    print("3. Выбрать героя!".center(width))
    print("4. Приказать героям биться на арене!".center(width))
    print("5. Выйти из игры!".center(width))
    print("")
    ans = input(f"{name} (угадано исходов арены: "
                f"{count_guess}/{num_arena - 1}) ----> ")
    while ans not in ["1", "2", "3", "4", "5"]:
        ans = input("Повторите ввод (от 1 до 5)! ---->")
    print(Style.RESET_ALL)
    clearConsole()
    return ans


def print_things(things: List[Thing]) -> None:
    clearConsole()

    for index, thing in enumerate(things):
        print(f"Артефакт № {index + 1}")
        print(thing)
    input("(Нажмите любую кнопку)")


def print_heroes(heroes: List[Union[Paladin, Warrior]]) -> None:
    print(Style.RESET_ALL)
    clearConsole()

    print("\nГерои и их характеристики")
    for index, hero in enumerate(heroes):
        print(f"Герой № {index + 1}")
        print(hero)
    input("(Нажмите любую кнопку)")


def print_arena(heroes: List[Union[Paladin, Warrior]],
                index_hero: int,
                ) -> int:
    clearConsole()
    width = os.get_terminal_size().columns
    print(Fore.RED + "БИТВА НАЧАЛАСЬ".center(width))
    print(Style.RESET_ALL)
    name_index_hero = heroes[index_hero - 1].name
    win_hero = arena(heroes)

    result_guess: int
    if name_index_hero == win_hero.name:
        print("Поздравляю! Вы угадали победителя ARENA!")
        result_guess = 1
    else:
        print(f"Сожалеем {name_index_hero} погиб на арене!")
        result_guess = 0
    input("\n(Нажмите любую кнопку)")
    return result_guess


def print_choose_hero(heroes: List[Union[Paladin, Warrior]]) -> int:
    width = os.get_terminal_size().columns

    clearConsole()

    index_hero = 100
    print(Fore.YELLOW +
          "\nГерои и их характеристики (c учетом артефактов)")
    for index, hero in enumerate(heroes):
        print("-" * (width // 4))
        print(f"Герой № {index + 1}")
        hero.print_statistic()
    list_index_hero = [str(i) for i in range(1, 11)]
    while index_hero not in list_index_hero:
        print("-" * (width // 4))
        index_hero = input(Fore.YELLOW +
                           "Выберите героя "
                           "(укажите номер героя от 1 до 10) - ")
    return int(index_hero)
