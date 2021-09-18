from random import shuffle

from colorama import Fore, Style

BASIC_HP = 50
BASIC_POWER = 15
BASIC_PROTECTION = 0.1


class Person:
    def __new__(cls, name: str):
        person = super().__new__(cls)
        print(f'Новый {cls.__name__} создан')
        return person

    def __init__(self, name,):
        self.name = name
        self.max_health = BASIC_HP
        self.current_health = BASIC_HP
        self.attack_power = BASIC_POWER
        self.protection = BASIC_PROTECTION
        self.things = []
        print(Fore.BLUE + f'{self} к бою готов!')
        print(Style.RESET_ALL)

    def set_things(self, list_things):
        shuffle(list_things)
        for thing in list_things:
            if len(self.things) < 4:
                self.things.append(thing)
                list_things.remove(thing)
                print(Fore.GREEN + f'{self} подобрал {thing.name}')
                self.max_health += thing.hp
                print(f'Здоровье увеличено на {thing.hp}')
                self.attack_power += thing.attack_power
                print(f'Сила урона увеличена на {thing.attack_power}')
                self.protection += thing.protection
                print(f'Процент защиты увеличен на {thing.protection}')
                print(Style.RESET_ALL)

    def attack(self, enemy):
        print(f'{self.name} атаковал {enemy.name}')
        damage = self.attack_power
        enemy.take_damage(self, damage)

    def take_damage(self, enemy, damage):
        attack_damage = damage - damage*self.protection
        print(f'{self.name} получил урона {attack_damage} от {enemy.name}')
        self.current_health -= attack_damage
        print(Fore.GREEN +
              f'Здоровье {self.name} {self.show_hp()}' +
              Style.RESET_ALL)

    def show_hp(self):
        return f'{self.current_health} из {self.max_health}'

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'

    def show(self):
        print(f'Герой:{self.name}',
              f'Здоровье:{self.max_health}',
              f'Сила урона:{self.attack_power}',
              f'Броня:{self.protection}',
              f'Предметы:{self.things}')


class Paladin(Person):
    def __init__(self, name,):
        super().__init__(name)
        self.max_health = BASIC_HP*2
        self.current_health = self.max_health
        self.protection = BASIC_PROTECTION*2


class Warrior(Person):
    def __init__(self, name,):
        super().__init__(name)
        self.attack_power = BASIC_POWER*2
        self.protection = BASIC_PROTECTION * 1.2


class Jedi(Person):
    def __init__(self, name,):
        super().__init__(name)
        self.attack_power = BASIC_POWER * 1.5
        self.max_health = BASIC_HP * 1.5
        self.current_health = self.max_health
        self.protection = BASIC_PROTECTION * 1.6
