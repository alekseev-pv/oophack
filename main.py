"""
Мини-проект "игра-арена"

Игра арена, на которую вы выпустите своих персонажей
и заставите их сражаться между собой. Играющая сама в себя
и выдающая вам только результат своей работы.

"""

from colorama import init, Fore

from functions import initial_heroes_and_things
from print_modul import (clearConsole, print_arena, print_choose_hero,
                         enter_name, print_heroes, print_things, start_menu)

if __name__ == "__main__":
    init()
    clearConsole()

    num_arena = 1
    count_guess = 0
    name = enter_name()
    ans = start_menu(name, num_arena, count_guess)
    heroes, things = initial_heroes_and_things()

    index_hero = 0
    while ans != "5":
        if ans == "1":
            print_heroes(heroes)
        elif ans == "2":
            print_things(things)
        elif ans == "3":
            index_hero = print_choose_hero(heroes)
        elif ans == "4":
            if index_hero == 0:
                print(Fore.RED +
                      "Перед началом сражения выберите героя (пункт № 3)")
                input("(Нажмите любую кнопку)")
            else:
                count_guess += print_arena(heroes, index_hero)
                heroes, things = initial_heroes_and_things()
                num_arena += 1
                index_hero = 0
        elif ans == "5":
            print("До свидания Уважаемый {name}")
            break
        ans = start_menu(name, num_arena, count_guess)
