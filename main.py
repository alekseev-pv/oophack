from random import randint, choice

import colorama
from colorama import Fore, Back, Style

colorama.init()

PERSONAGE_COLORS = (Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN)
CHARACTERISTICS = ['ботан', 'сирота', 'бездомный', 'программист', 'курит',
                   'смотрит сериалы', 'любит котиков', 'готовит кексики',
                   'участник шоу "Битва экстрасенсов"', 'храпит', 'свистит',
                   'выпивает 10 чашек кофе в день', 'интересуется политикой',
                   'нет слуха', 'есть секрет', 'знает албанский', 'рыбак',
                   'всегда говорит правду', 'играет со спичками', 'депутат']
PERSONAGES = ['Илон Маск', 'Ксения Собчак', '', '', '', 'Трамп', '', '', 'Роналду', '', '', '', '', '', '', '', '', '', '', '', ]


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
    ):
        self.name = name
        self.health = health
        self.current_hp = health
        self.damage = damage
        self.final_damage = damage
        self.defense = defense
        self.final_defense = defense
        self.color = choice(PERSONAGE_COLORS)
        self.things = []
        print(f'Персонаж {self} появился в этом мире!')
        print(f'Его параметры: Здоровье - {self.health}, '
              f'урон - {self.damage}, защита - {self.defense}')

    def __str__(self):
        return f'{self.color}{self.name}{Style.RESET_ALL}'

    def attack(self, enemy: 'Person'):
        """
        Нанесение урона другому персонажу - атака.
        """
        print(f'{Fore.RED}↔ {self} {Fore.RED}атакует{Style.RESET_ALL} {enemy}')
        enemy.gets_damage(self, self.damage)

    def gets_damage(self, enemy: 'Person', attack_damage: int):
        """
        Получение урона и расчёт оставшегося здоровья.
        """
        total_damage = attack_damage * enemy.defense
        self.current_hp -= total_damage
        print(f'└─ {self} получает урон от {enemy}: '
              f'{Fore.RED}{total_damage}{Style.RESET_ALL}.', end='')
        # print(self.current_hp, enemy.defense)
        print(f' У него остаётся '
              f'{Fore.GREEN}{self.current_hp}{Style.RESET_ALL} здоровья')

    def set_thing(self, thing):
        """
        Присваивает предмет персонажу.
        """
        self.things.append(thing)
        print(f'{Fore.MAGENTA}◙{Style.RESET_ALL} {self} получил {thing}')
        self.current_hp = self.health + (
                self.health * self.summary_parameter('health')
        )
        print(f'└─ Теперь его Здоровье: {self.current_hp}', end='. ')
        self.final_damage = self.damage + (
                    self.damage * self.summary_parameter('damage')
        )
        print(f'Урон: {self.final_damage}', end='. ')
        self.final_defense = self.defense + (
                    self.defense * self.summary_parameter('defense')
        )
        print(f'Защита: {self.final_defense}')
        all_things = self.all_things()
        print(f'└─ Все его предметы: '
              f'{Fore.MAGENTA}{all_things}{Style.RESET_ALL}')

    def all_things(self):
        """Список всех предметов персонажа."""
        things_list = [item.name for item in self.things]
        return ', '.join(things_list)

    def set_things(self, things_list):
        """
        Присваивает список вещей персонажу.
        """
        for thing in things_list:
            self.set_thing(thing)

    def summary_parameter(self, characteristic):
        """
        Суммирование значений указанной харатеристики для всех
        надетых на персонажа предметов.
        """
        if characteristic == 'health':
            return sum([item.health for item in self.things])
        if characteristic == 'damage':
            return sum([item.damage for item in self.things])
        if characteristic == 'defense':
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
    ):
        super().__init__(name, health, damage, defense)
        self.health = health * 2
        self.defence = defense * 2
        # print(f'Персонаж {self.name} класса паладин появился в этом мире!')


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
    ):
        super().__init__(name, health, damage, defense)
        self.damage = damage * 2
        # print(f'Персонаж {self.name} класса появился в этом мире!')


def duel(player1: Person, player2: Person):
    priority = ((player1, player2), (player2, player1))
    previous_priority = None
    while True:
        # кто кого атакует
        current_priority = priority[randint(0, 1)]
        # если очерёдность опять та же...
        if (previous_priority is not None) and (
                previous_priority == current_priority
        ):
            print(f'└─ {defending} ошеломлён, и вновь ')
        attacker, defending = current_priority
        attacker.attack(defending)
        # если персонаж мёртв...
        if attacker.is_dead:
            print(f'{Fore.WHITE}{Back.BLACK}▄ ╬ ▄ {attacker}'
                  f'{Fore.WHITE}{Back.BLACK} погибает{Style.RESET_ALL}')
            break
        if defending.is_dead:
            print(f'{Fore.WHITE}{Back.BLACK}▄ ╬ ▄ {defending}'
                  f'{Fore.WHITE}{Back.BLACK} погибает{Style.RESET_ALL}')
            break
        previous_priority = current_priority


def main():
    thing1 = Thing('Странное кольцо', health=0.1, damage=-0.05, defense=-0.1)
    thing2 = Thing('Утюг', health=0.05, damage=0.25, defense=0.05)
    thing3 = Thing('Клубок ниток', health=0.15, damage=-0.01, defense=0.01)
    thing4 = Thing('Метла', health=0.1, damage=0.1, defense=0.1)
    player1 = Person(name='Шерлок', health=100, damage=35, defense=1)
    player2 = Paladin(name='Мориарти', health=100, damage=40, defense=0.95)
    # player1.set_thing(thing1)
    player1.set_things([thing1, thing2])
    player2.set_thing(thing3)
    player1.set_thing(thing4)
    # print(thing1)
    # player1.attack(player2)
    duel(player1, player2)


if __name__ == '__main__':
    main()
