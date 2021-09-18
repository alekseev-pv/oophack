from random import randint, choice, sample, shuffle

import colorama
from colorama import Fore, Back, Style

colorama.init()

PERSONAGE_COLORS = (Fore.GREEN, Fore.BLUE, Fore.CYAN)
CHARACTERISTICS = ('ботан', 'сирота', 'бездомный', 'программист', 'курит',
                   'смотрит сериалы', 'любит котиков', 'готовит кексики',
                   'участник шоу "Битва экстрасенсов"', 'храпит', 'свистит',
                   'выпивает 10 чашек кофе в день', 'интересуется политикой',
                   'нет слуха', 'есть секрет', 'знает албанский', 'рыбак',
                   'всегда говорит правду', 'играет со спичками', 'депутат')
PERSONAGES = ('Илон Маск', 'Ксения Собчак', 'Моргенштерн', 'Ольга Бузова',
              'Бейонсе', 'Трамп', 'Гарри Поттер', 'Павел Дуров', 'Терминатор',
              'Нео', 'Линк', 'Леди Гага', 'Баба Яга', 'Шрек', 'Грязный Гарри',
              'Бэтмен', 'Павел Алексеев', 'Джек Воробей', 'Роналду', 'Джокер')
THINGS_NAMES = ('Утюг', 'Метла', 'Клубок ниток', 'Странное кольцо', 'Молоток',
                'Скейтборд', 'Ноутбук', 'Тапки', 'Сапоги', 'Белый халат',
                'Баян', 'Дудочка', 'Сковорода', 'Букварь', 'Пилочка', 'Коврик',
                'Базука', 'Рояль', 'Книга "Изучаем Python. Марк Лутц"', 'Яд',
                'Биткоин', 'Свисток', 'Волшебная палочка', 'Губка', 'Наушники')


class Thing:
    """
    Предмет и его характеристики.
    name: название
    defense: процент к защите
    damage: процент к урону
    health: процент к здоровью.
    """

    def __init__(
            self,
            name: str,
            health: float,
            damage: float,
            defense: float,
    ):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        print(f'Предмет {Fore.MAGENTA}{self}{Style.RESET_ALL} '
              f'кем-то создан, но пока не обрёл своего хозяина')
        print(f'Модификаторы предмета: Здоровье {self.health}, '
              f'урон {self.damage}, защита {self.defense}')

    def __str__(self):
        return f'{Fore.MAGENTA}{self.name}{Style.RESET_ALL}'


class Person:
    """
    Персонаж и его характеристики.
    name: имя
    health: здоровье
    current_hp: текущее здоровье
    damage: базовая атака
    defense: базовый процент защиты
    things: список вещей, принадлежащих персонажу.
    """

    def __init__(
            self,
            name: str,
            health: float,
            damage: float,
            defense: float,
            characteristic: str
    ):
        self.name = name
        self.health = health
        self.current_hp = health
        self.damage = damage
        self.final_damage = damage
        self.defense = defense
        self.final_defense = defense
        self.color = choice(PERSONAGE_COLORS)
        self.characteristic = characteristic
        self.things = []
        print(f'{self} появился в этом мире!')
        print(f'Параметры персонажа: Здоровье - {self.health}, '
              f'урон - {self.damage}, защита - {self.defense}')
        print(f'{Fore.YELLOW}Особенность: {self.characteristic}{Style.RESET_ALL}')

    def __str__(self):
        return f'{self.color}{self.name}{Style.RESET_ALL}'

    def attack(self, enemy: 'Person'):
        """
        Нанесение урона другому персонажу - атака.
        """
        print(f'{Fore.RED}↔ {self} {Fore.RED}атакует{Style.RESET_ALL} {enemy}')
        enemy.gets_damage(self, self.damage)

    def gets_damage(self, enemy: 'Person', attack_damage: float):
        """
        Получение урона и расчёт оставшегося здоровья.
        """
        total_damage = attack_damage * enemy.defense
        self.current_hp = round(self.current_hp - total_damage, 2)
        print(f'└─ {self} получает урон от {enemy}: '
              f'{Fore.RED}{total_damage}{Style.RESET_ALL}.', end='')
        # print(self.current_hp, enemy.defense)
        if self.current_hp > 0:
            print(f' У него остаётся '
                  f'{Fore.GREEN}{self.current_hp}{Style.RESET_ALL} здоровья')

    def set_thing(self, thing):
        """
        Присваивает предмет персонажу.
        """
        self.things.append(thing)
        print(f'{Fore.MAGENTA}◙{Style.RESET_ALL} {self} получил {thing}')
        self.current_hp = round(self.health + (
                self.health * self.summary_parameter('health')
        ), 2)
        print(f'└─ Теперь его Здоровье: {self.current_hp}', end='. ')
        self.final_damage = round(self.damage + (
                self.damage * self.summary_parameter('damage')
        ), 2)
        print(f'Урон: {self.final_damage}', end='. ')
        self.final_defense = round(self.defense + (
                self.defense * self.summary_parameter('defense')
        ), 2)
        print(f'Защита: {self.final_defense}')

    def all_things(self):
        """Список всех предметов персонажа."""
        things_list = ', '.join([item.name for item in self.things])
        print(f'└─ Все его предметы: '
              f'{Fore.MAGENTA}{things_list}{Style.RESET_ALL}')

    def set_things(self, things_list):
        """
        Присваивает список вещей персонажу.
        """
        for thing in things_list:
            self.set_thing(thing)

    def summary_parameter(self, parameter):
        """
        Суммирование значений указанной харатеристики для всех
        надетых на персонажа предметов.
        """
        if parameter == 'health':
            return sum([item.health for item in self.things])
        if parameter == 'damage':
            return sum([item.damage for item in self.things])
        if parameter == 'defense':
            return sum([item.defense for item in self.things])
        return 0

    @property
    def is_dead(self):
        return self.current_hp <= 0


class Paladin(Person):
    """
    Паладин.
    """

    def __init__(
            self,
            name: str,
            health: float,
            damage: float,
            defense: float,
            characteristic: str
    ):
        super().__init__(name, health, damage, defense, characteristic)
        self.health = health * 2
        self.defence = defense * 2
        print('Здоровье и защита увеличены вдвое!')


class Warrior(Person):
    """
    Воин.
    """
    def __init__(
            self,
            name: str,
            health: float,
            damage: float,
            defense: float,
            characteristic: str
    ):
        super().__init__(name, health, damage, defense, characteristic)
        self.damage = damage * 2
        print('Урон увеличен вдвое!')


def duel(player1: Person, player2: Person):
    """
    Поединок двух персонажей длится до смерти одного из них.
    """
    priority = ((player1, player2), (player2, player1))
    previous_priority = None
    while True:
        # кто кого атакует
        current_priority = priority[randint(0, 1)]
        # если очерёдность опять та же...
        if (previous_priority is not None) and (
                previous_priority == current_priority
        ):
            print(f'└─ {defender} ошеломлён, и вновь ')
        attacker, defender = current_priority
        attacker.attack(defender)
        # если персонаж мёртв...
        if attacker.is_dead:
            print(f' {Fore.WHITE}{Back.BLACK}▄ ╬ ▄ {attacker}'
                  f'{Fore.WHITE}{Back.BLACK} погибает{Style.RESET_ALL}\n')
            return defender.name
        if defender.is_dead:
            print(f' {Fore.WHITE}{Back.BLACK}▄ ╬ ▄ {defender}'
                  f'{Fore.WHITE}{Back.BLACK} погибает{Style.RESET_ALL}\n')
            return attacker.name
        previous_priority = current_priority


def generate_things():
    """
    Генератор вещей.
    """
    # генерируем от 10 до 40 вещей, чтобы не более 4 одному.
    count = randint(10, 40)
    things = []
    for i in range(count):
        # берём слуайное название вещи из списка
        number_thing = randint(0, len(THINGS_NAMES) - 1)
        things.append(
            Thing(
                name=THINGS_NAMES[number_thing],
                health=round(-0.25 + (randint(0, 50) / 100), 2),
                damage=round(-0.25 + (randint(0, 50) / 100), 2),
                defense=round(-0.1 + (randint(0, 20) / 100), 2),
            )
        )
        print()
    return things


def generate_personages():
    """
    Генератор персонажей.
    """
    count = 10
    players = []
    # выбираем случайные имена персонажей из списка
    ten_names = sample(PERSONAGES, count)
    # выбираем случайные особенности персонажей из списка
    ten_characteristics = sample(CHARACTERISTICS, count)
    for i in range(count):
        # случайный класс персонажа - обычный, паладин или воин
        class_personage = choice([Person, Paladin, Warrior])
        players.append(
            class_personage(
                name=ten_names[i],
                health=round(100 - randint(0, 30), 2),
                damage=round(40 - randint(0, 20), 2),
                defense=round(1 - (randint(0, 15) / 100), 2),
                characteristic=ten_characteristics[i]
            )
        )
        print()
    return players


def distribution_items(players, things):
    """
    Раздача предметов - не более 4 в одни руки.
    (хм, а если у персонажа 4 руки, значит можно вдвое больше?).
    """
    # порядковый номер последнего отданного предмета
    current = 0
    for player in players:
        # случайное количество предметов
        count = randint(1, 4)
        player.set_things(things[current:current + count])
        current += count
        player.all_things()


def battle(players):
    """
    Турнир - персонажи делятся на две команды и соревнуются.
    """
    count_players = 10
    winner_players = []
    # перемешиваем участников и потом берём попарно
    shuffle(players)
    command1 = players[0:5]
    command2 = players[5:10]
    for i in range(5):
        winner = duel(command1[i], command2[i])
        winner_players.append(winner)
    list_winners = ', '.join(winner_players)
    print(f'{Fore.YELLOW}{Back.BLUE}Победители турнира: {list_winners}{Style.RESET_ALL}')


def main():
    things = generate_things()
    players = generate_personages()
    distribution_items(players, things)
    print()
    print(f'{Fore.WHITE}{Back.RED}▒▒▒▒ Начинается битва ▒▒▒▒{Style.RESET_ALL}')
    print()
    battle(players)


if __name__ == '__main__':
    main()
