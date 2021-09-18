from colorama import Fore, Style
import time

import sys

from arena import Arena
from things import Thing


class Menu:
    """Представление меню."""

    def __init__(self, arena):
        self.arena = arena()
        self.choices = {
            '1': self.run_game,
            '2': self.exit
        }

    def display_menu(self):
        """Метод выводит на экран меню."""
        print('Добро пожаловать в игру!')
        print('Нажми ' + Fore.BLUE + '1' + Style.RESET_ALL +
              ' чтобы начать игру')
        print('Нажмите ' + Fore.CYAN + '2' + Style.RESET_ALL + ' чтобы выйти')
        print()

    def start(self):
        """Метод запускает меню."""
        while True:
            self.display_menu()
            choice = input(f'{Fore.BLUE}Выберите вариант{Style.RESET_ALL}  ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{Fore.RED}Неверный ввод {choice}{Style.RESET_ALL}')

    def run_game(self):
        """Метод запускает игру."""
        active = True
        self.arena.generate_random_thing(Thing)
        self.arena.player_set_up()
        self.arena.generate_characters_for_computer(['warrior', 'paladin', 'dwarf'])

        while active:
            # Игрок атакует
            self.arena.print_players_team()
            print(f'{Fore.RED}Вы атакуете!{Style.RESET_ALL}')

            attacker_index = self.arena.read_user_character_input() - 1
            attacker = self.arena.team1[attacker_index]
            defender = self.arena.team2.pop(
                self.arena.get_index_of_character_with_maximum_attribute('final_defence'))
            self.arena.game_round(attacker, defender)
            time.sleep(2)
            if defender.hp > 0:
                self.arena.team2.append(defender)
            else:
                print(f'{Fore.RED}Вы убили{Style.RESET_ALL} {defender.name}!')
                time.sleep(2)
            if self.arena.is_over():
                active = False
                time.sleep(2)
                continue
            # Игрок защищается
            attacker = self.arena.team2[
                self.arena.get_index_of_character_with_maximum_attribute('final_attack')]
            self.arena.print_players_team()

            print(f'{Fore.GREEN}Теперь вы защищаетесь!{Style.RESET_ALL}')
            defender_index = self.arena.read_user_character_input() - 1
            defender = self.arena.team1.pop(defender_index)

            self.arena.game_round(attacker, defender)
            time.sleep(2)
            if defender.hp > 0:
                self.arena.team1.append(defender)
            else:
                print(f'{Fore.RED}Ващего персонажа {Style.RESET_ALL}{defender.name} убили!')
                time.sleep(2)
            if self.arena.is_over():
                active = False

    def exit(self):
        sys.exit(1)


def main():
    menu = Menu(arena=Arena)

    menu.start()


if __name__ == '__main__':
    main()
