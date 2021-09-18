import colorama
import names
import random

from colorama import Back, Fore, Style


class Thing:
    """
    Класс Thing описывает игровые вещи
    """

    def __init__(self, name,
                 defence_per, attack_per, hp_per) -> None:
        """
        Принимает на вход:
        name - имя вещи,
        defence_per - процент защиты,
        attack_per - процент нападения,
        hp_per - жизнь.
        """
        self.name = name
        self.defence_per = round(defence_per, 2)
        self.attack_per = round(attack_per, 2)
        self.hp_per = round(hp_per, 2)

    def __str__(self) -> str:
        return (f'Имя: {self.name} '
                f'Защита: {self.defence_per} '
                f'Нападение:{self.attack_per} '
                f'Жизнь:{self.hp_per}')


class Person:
    """
    Класс Person описывает основные параметры персонажа игры
    """

    def __init__(self, name,
                 hp, base_attack, base_defence) -> None:
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.finalProtection = 0
        self.things = []

    def set_things(self, things):
        """
        Вооружает война, определяет максимальную защитную способность
        """
        self.things = things
        self.finalProtection = self.get_final_protection()
        pass

    def get_final_protection(self):
        """
        Возвращает максимальную защитную способность
        """
        return self.base_defence + self.get_things_protection()

    def get_things_protection(self):
        """
        Возвращает защитную способность вооружения
        """
        return sum([x.defence_per for x in self.things])

    def got_attacked(self, attack_damage):
        """
        Рассчитывает значение жизни после атаки
        """
        self.hp = (self.hp - (attack_damage -
                   attack_damage*self.finalProtection))

    def attack(self):
        """
        Определяет урон при атаке
        """
        selected_thing = self.things[random.randint(
            0, len(self.things) - 1)]
        return selected_thing.attack_per * self.base_attack

    def is_alive(self):
        """
        Возвращает жив ли воин
        """
        if self.hp <= 0:
            return False
        return True


class Paladin(Person):
    """
    Класс Paladin увеличивает оборонительные способности Персонажа
    """

    def __init__(self, name, hp, base_attack, base_defence) -> None:
        super().__init__(name, hp, base_attack, base_defence)
        self.hp = self.hp*2
        self.base_defence = self.base_defence * 2


class Warrior(Person):
    """
    Класс Warrior увеличивает наступательные способности Персонажа
    """

    def __init__(self, name, hp, base_attack, base_defence) -> None:
        super().__init__(name, hp, base_attack, base_defence)
        self.base_attack = self.base_attack * 2


class Game():
    def __init__(self) -> None:
        self.things = []

    def create_all_things(self):
        for i in range(20):
            name = f'{names.get_last_name()}_thing'
            defence = random.uniform(0, 0.1)
            attack = random.uniform(0.01, 0.1)
            hp = random.uniform(0, 0.1)
            self.things.append(Thing(name, defence, attack, hp))
        self.things.sort(key=lambda x: x.defence_per)
        return self.things

    def get_random_things(self, all_things):
        return [all_things[i] for i in range(random.randint(1, 4))]

    def battle(self, first_warrior, second_warrior):
        colorama.init()
        print(Back.GREEN + Fore.YELLOW + f'Бой между {first_warrior.name} и '
              f'{second_warrior.name} начинается!')
        print(Style.RESET_ALL)
        first_warrior.hp = 100
        second_warrior.hp = 100
        while True:
            print(f'{first_warrior.name} здоровья: '
                  f'{round(first_warrior.hp,2)}')
            print(f'{second_warrior.name} здоровья: '
                  f'{round(second_warrior.hp,2)}')

            warrior_damage = round(first_warrior.attack(), 2)
            print(Back.YELLOW + Fore.RED +
                  f'{first_warrior.name} наносит удар по '
                  f'{second_warrior.name} на {warrior_damage} урона' +
                  Style.RESET_ALL)
            second_warrior.got_attacked(warrior_damage)
            if not second_warrior.is_alive():
                print(f'{first_warrior.name} победил')
                return second_warrior
            warrior_damage = round(second_warrior.attack(), 2)
            print(Back.BLUE + Fore.RED +
                  f'{second_warrior.name} наносит удар по '
                  f'{first_warrior.name} на {warrior_damage} урона' +
                  Style.RESET_ALL)
            first_warrior.got_attacked(warrior_damage)
            if not first_warrior.is_alive():
                print(f'{second_warrior.name} победил' + Style.RESET_ALL)
                return first_warrior

    def auto_game(self, warrior_names, warrior_types, person=None):
        all_things = self.create_all_things()  # произвольноe количество вещей
        warrior_names = [f'{names.get_first_name()}_warrior'
                         for i in range(20)]  # список имен персонажей
        warriors = [warrior_types[random.randint(0, 1)](
            warrior_names[random.randint(
                0, len(warrior_names)-1)], 100, random.randint(10, 100),
            random.uniform(0.01, 0.1)) for i in range(0, 10)]  # список войнов
        if person is not None:
            warriors.append(person)
        for warrior in warriors:
            warrior.set_things(self.get_random_things(all_things))
        while len(warriors) != 1:
            first_warrior = warriors[random.randint(
                0, len(warriors)-1)]
            second_warrior = warriors[random.randint(
                0, len(warriors)-1)]
            while second_warrior == first_warrior:
                second_warrior = warriors[random.randint(
                    0, len(warriors)-1)]
            lost_warrior = self.battle(first_warrior, second_warrior)
            warriors.remove(lost_warrior)
        print(f'{warriors[0].name} победил')


def main() -> None:
    game = Game()
    warrior_names = [f'{names.get_first_name()}_warrior'
                     for i in range(20)]  # список имен персонажей
    warrior_types = [Paladin, Warrior]  # тип война
    game_type = input(
        'Выберите тип игры 1 - симуляция, 2 - создать персонажа\n')
    if game_type == '1':
        game.auto_game(warrior_names, warrior_types)
    else:
        name = input('Введите имя песонажа\n')
        things = game.create_all_things()
        for thing in things:
            print(thing)
        selected_things_name = input(
            'Введите через пробел имена вооружений, не более 4\n').split(' ')
        selected_things = list(
            filter(lambda x: x.name in selected_things_name, things))
        race = warrior_types[int(
            input('Если вы Paladin введите 1, если Warrior то 2\n'))-1]
        attack = int(input('Определите уровень атаки от 1 до 100\n'))
        defence = int(input('Определите уровень защиты от 1 до 99\n'))/100
        person = race(name, 100, attack, defence)
        person.set_things(selected_things)
        game.auto_game(warrior_names, warrior_types, person)


if __name__ == '__main__':
    main()
