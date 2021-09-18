from random import sample

from tabulate import tabulate
import colorama
from colorama import Fore

from config import NUMBER_PLAYERS, SEPARATOR_LENGTH
from characters import generate_players

colorama.init(autoreset=True)


class Game():

    def __init__(self):
        self.players = generate_players()
        self.graveyard = []

    def show_introduction(self):
        print()
        print(f'{Fore.GREEN}Что? Где? Когда?  {Fore.RED}СМЕРТЕЛЬНАЯ БИТВА!')
        print()
        print('...звучит музыка...')
        print(f'{Fore.CYAN}Что наша жизнь? ИГРА!')
        print()
        print(f'{Fore.YELLOW}За столом cегодня играют:')
        print('*'*SEPARATOR_LENGTH)
        print()

        for player in self.players:
            player_things = ', '.join([thing.title for thing in player.things])
            print(f'Обладатель {Fore.BLUE}{player_things}')
            print(f'{Fore.GREEN}{player.name}.')
            print(f'(Атака {player.damage:.0f}, Защита {player.protection:.2f}'
                  f', Здоровье {player.health_point:.0f}, {player.class_name})'
                  )
            print('*'*SEPARATOR_LENGTH)

    def play_main_part(self):
        for game_round in range(1, NUMBER_PLAYERS):
            print(f'{Fore.YELLOW}Играем до последнего знатока')
            print(f'{Fore.YELLOW}Счет 0 : {len(self.graveyard)}')
            print(f'{Fore.YELLOW}{game_round} раунд!')
            print()

            while True:
                attacker, defender = sample(self.players, 2)
                attack_damage = attacker.attack(defender)
                print(f'{Fore.GREEN}{attacker.name} {Fore.RESET}атакует '
                      f'{Fore.GREEN}{defender.name}{Fore.RESET}'
                      f' и наносит {Fore.RED}{attack_damage:.0f} урона.')
                if defender.is_alive:
                    print(f'{defender.name} выживает на '
                          f'{defender.health_point:.0f} хп.')
                else:
                    self.graveyard.append(defender)
                    self.players.remove(defender)
                    print(f'К сожалению, {Fore.GREEN}{defender.name}'
                          f'{Fore.RESET} не выдерживает и '
                          f'{Fore.CYAN}"покидает наш стол"')
                    break
                print()
            print()
            print('*'*SEPARATOR_LENGTH)
            print()
        last_man_standing = self.players.pop()
        self.graveyard.append(last_man_standing)
        print('Сегодняшний победитель, единственный кто удержался за столом')
        print()
        print(f'{Fore.GREEN}{last_man_standing.name.upper()}')
        print()
        print(f'{Fore.CYAN}Звучит песня Тамары Гвердцители - Виват король')
        print()

    def print_final_state(self):
        headers = ['Место', 'Игрок', 'Атака', 'Защита', 'Здоровье',
                   'Урон нанесено', 'Урон полученно', 'Класс']
        game_result = []
        place = 0
        for player in reversed(self.graveyard):
            place += 1
            game_result.append([
                place,
                player.name,
                round(player.damage),
                round(player.protection, 2),
                round(player.init_health_point),
                round(player.damage_dealt),
                round(player.damage_taken),
                player.class_name,
            ])
        print('По экрану проплывают результаты игры.')
        print(tabulate(game_result, headers, tablefmt="grid"))

    def run(self):
        self.show_introduction()
        self.play_main_part()
        self.print_final_state()


game = Game()
game.run()
