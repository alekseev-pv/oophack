import time
from colorama import Style, Fore

import random
import names
from characters import Warrior, Paladin, Dwarf

CHAR_NAME_LIST = []
THINGS_NAMES = ['кольцо', 'посох', 'волшебная палочка', 'плащ', 'посох']
for i in range(20):
    CHAR_NAME_LIST.append(names.get_first_name())


class Arena:
    """Класс арена."""
    CHARACTERS = {
        'warrior': {'class': Warrior,
                    'description': 'В два раза больше здоровья'},
        'paladin': {'class': Paladin,
                    'description': 'В два раза больше здоровья и атаки'},
        'dwarf': {'class': Dwarf,
                  'description': 'В два раза больше здоровья и защиты, но в два раза меньше атаки'},
    }

    def __init__(self):
        self.team1 = []
        self.team2 = []
        self.things = []

    def _add_to_team1(self, obj):
        """Добавить персонажа в команду 1."""
        self.team1.append(obj)

    def _add_to_team2(self, obj):
        """Доабвить персонажа в команду 2."""
        self.team2.append(obj)

    def _generate_character(self, character):
        """Сгенерировать персонажа заданного типа. Если передан список, то
        тогда генерируется рандомного типа.
        """
        if isinstance(character, list):
            char_name = random.choice(character)
            char = self.CHARACTERS.get(char_name).get('class')
        else:
            char = self.CHARACTERS.get(character).get('class')
        things = []
        if self.things:
            things = random.choices(self.things, k=random.randint(0, 4))
        new_char = char(
            name=random.choice(CHAR_NAME_LIST),
            hp=100,
            base_attack=random.randint(100, 200),
            base_defence=random.uniform(0.01, 0.3),
            things=things
        )
        new_char.set_final_hp()

        return new_char

    def _create_players_team(self, character_dict):
        """Создать команду игроку.
        Принимает словарь - {'название класса': количество}."""
        for character, quantity in character_dict.items():
            for _ in range(quantity):
                new_char = self._generate_character(character)
                self._add_to_team1(new_char)

    def generate_random_thing(self, Thing):
        """Сгенерировать случайное количесво магических предметов."""
        for _ in range(random.randint(1, 100)):
            new_thing = Thing(
                name=random.choice(THINGS_NAMES),
                defence=random.uniform(0.001, 0.1),
                attack=random.randint(0, 3),
                hp=1
            )
            self.things.append(new_thing)
        self.things = sorted(self.things, key=lambda obj: obj.defence)

    def generate_characters_for_computer(self, available_characters_list):
        """Сгенерировать команду для компьютера случайным образом."""
        for _ in range(10):
            new_char = self._generate_character(
                available_characters_list)
            self._add_to_team2(new_char)

    def print_players_team(self):
        """Напечатать команду игрока."""
        print(f'У тебя в команде: ')
        print('***************')
        for count, char in enumerate(self.team1):
            print(f'{Fore.CYAN}Номер: {Style.RESET_ALL}{count + 1},'
                  f'{Fore.GREEN} Имя: {Style.RESET_ALL}{char.name},'
                  f'{Fore.BLUE} HP{Style.RESET_ALL} {char.hp}, '
                  f'{Fore.RED}Атака{Style.RESET_ALL} {char.final_attack}, '
                  f'{Fore.YELLOW}Защита{Style.RESET_ALL} {int(char.final_defence * 100)}%')
            print('*****')

    def print_available_characters(self):
        """Печатает, какие персонажи зарегестрированы в игре."""
        for key in self.CHARACTERS.keys():
            print(
                f'{Fore.RED}{key}{Style.RESET_ALL}: {self.CHARACTERS[key]["description"]}')
            print('**')

    def player_set_up(self):
        """Метод для настройки команды игрока."""
        total = 10
        print(f"""
        Давай соберем команду
        Команда будет состоять из {total} персонажей.
        Доступны классы: 
        
        """)
        self.print_available_characters()

        character_dict = {}

        for char_name in self.CHARACTERS.keys():
            active = True
            while active:
                if total == 0:
                    active = False
                    continue
                char_quantity = input(
                    f'Сколько хочешь {Fore.YELLOW}{char_name}{Style.RESET_ALL}, '
                    'Осталось: '
                    f'{Fore.RED}{total}{Style.RESET_ALL} ')
                try:
                    char_quantity = int(char_quantity)
                except ValueError:
                    print(
                        f'{Fore.RED}Неверный тип данных{Style.RESET_ALL}')
                    continue

                if char_quantity > total or char_quantity < 0:
                    print(f'Ты не можешь взять '
                          f'столько войнов, или неправильный тип данных')
                    continue
                if char_quantity == 0:
                    break
                total -= char_quantity
                character_dict[char_name] = char_quantity
                break

        # Если пользователь почему-то не выбрал ни одного персонажа, то даем рандомных
        if not character_dict.keys():
            print('Ты не выбрал ни одного персонажа, поэтому тебе дадут их рандомно!')
            time.sleep(2)
            for _ in range(10):
                new_char = self._generate_character(['warrior',
                                                     'dwarf',
                                                     'paladin'])
                self._add_to_team1(new_char)
            return None


        print(f"""
            Итак, ты собрал команду!
            *********
            """)
        for key, value in character_dict.items():
            print(
                f'{Fore.BLUE}{key}{Style.RESET_ALL}: {Fore.RED}{value}{Style.RESET_ALL}'
                )

        self._create_players_team(character_dict)
        time.sleep(2)

    def read_user_character_input(self):
        """Считать номер персонажа."""
        while True:
            try:
                char_pos = int(input(
                    f'Введите {Fore.RED}номер{Style.RESET_ALL} персонажа для выбора '))
                if char_pos > len(self.team1):
                    print(
                        f'Номера {Fore.RED}{char_pos}{Style.RESET_ALL} нет в команде')
                    continue
                return char_pos
            except ValueError:
                print(f'{Fore.RED}Неправильный тип данных{Style.RESET_ALL}')
                continue

    def game_round(self, attacker, defender):
        """Один игровой раунд."""
        attack_damage = attacker.final_attack
        final_defence = defender.final_defence
        final_damage = attack_damage - attack_damage * final_defence
        final_damage = round(final_damage, 2)
        defender.hp -= final_damage
        print(
            f'Персонаж {attacker.name} наносит {Fore.RED}урон {final_damage}{Style.RESET_ALL}'
            f' {Fore.BLUE}персонажу {defender.name}{Style.RESET_ALL}')

    def get_index_of_character_with_maximum_attribute(self, attribute):
        """Получить индекс персонажа с максимальным значением атрибута."""
        max_index = 0
        max_attribute = 0
        for k in range(0, len(self.team2)):

            if getattr(self.team2[k], attribute) > max_attribute:
                max_index = k
                max_attribute = getattr(self.team2[k], attribute)
        return max_index

    def is_over(self):
        """Проверка, зкончилась ли игра."""
        if not self.team1:
            print(f'{Fore.BLUE}К сожалению, вы проиграли!{Style.RESET_ALL}')
            return True
        if not self.team2:
            print(f'{Fore.RED}Поздравляем, вы победили!{Style.RESET_ALL}')
            return True
        return False
