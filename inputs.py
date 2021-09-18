from colorama import Fore, init

import messages
import solo_adventure

init(autoreset=True)


def main_menu():
    x = input()
    if x == 'help':
        messages.help()
    elif x == 'arena':
        messages.arena()
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    elif x == 'solo':
        messages.solo_menu()
    else:
        print(Fore.RED + 'Неожиданная команда!')
        main_menu()


def solo_menu():
    x = input()
    if x == 'paladin':
        solo_adventure.Adventure('paladin')
    elif x == 'warrior':
        solo_adventure.Adventure('warrior')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        solo_menu()


def solo_start(adventure):
    x = input()
    if x == 'tavern':
        messages.tavern_1(adventure)
    elif x == 'children':
        messages.children_1(adventure)
    elif x == 'inventory':
        messages.inventory(adventure)
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        solo_menu(adventure)


def children_talk(adventure):
    x = input()
    if x == 'pub':
        messages.children_talk_pub(adventure)
    elif x == 'elder':
        messages.children_talk_elder(adventure)
    elif x == 'dream':
        messages.children_talk_dream(adventure)
    elif x == 'leave':
        messages.children_talk_leave(adventure)
    elif x == 'inventory':
        messages.inventory(adventure)
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        children_talk(adventure)


def solo_main_place(adventure):
    x = input()
    if x == 'tavern':
        messages.tavern_1(adventure)
    elif x == 'elder' and adventure.elder:
        messages.elder(adventure)
    elif x == 'elder+' and adventure.elder2:
        messages.elder2(adventure)
    elif x == 'witch' and adventure.witch:
        messages.witch(adventure)
    elif x == 'inventory':
        messages.inventory(adventure)
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        solo_main_place(adventure)


def tavern_1(adventure):
    x = input()
    if x == 'dream':
        messages.tavern_1_dream(adventure)
    elif x == 'elder':
        messages.tavern_1_elder(adventure)
    elif x == 'rest':
        messages.tavern_1_rest(adventure)
    elif x == 'leave':
        messages.solo_main_place(adventure)
    elif x == 'inventory':
        messages.inventory(adventure)
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        tavern_1(adventure)


def nice():
    x = input()
    if not x == 'nice':
        nice()


def elder3(adventure):
    x = input()
    if x == 'dream':
        messages.elder_dream(adventure)
    elif x == 'leave':
        messages.solo_main_place(adventure)
    elif x == 'inventory':
        messages.inventory(adventure)
    elif x == 'q' or x == 'quit':
        print(Fore.GREEN + 'Удачного дня!')
    else:
        print(Fore.RED + 'Неожиданная команда!')
        elder3(adventure)
