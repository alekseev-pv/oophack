from random import randint
from gear import Thing
from typing import List
from time import sleep

MIN_PCT = 1
MAX_PCT = 100
MIN_BASE_HP = 20
MAX_BASE_HP = 100
MAX_BASE_ATACK = MAX_BASE_PROTECTION = 15
MIN_BASE_ATACK = MIN_BASE_PROTECTION = 2
BASE_PRECISION = BASE_CRIT = 10
class Person:
    ''' Персонаж'''
    def __init__(
        self,
        name: str,
        hp: int,
        base_atack: int,
        base_protection: int, 
    ):
        assert hp in range(MIN_BASE_HP, MAX_BASE_HP+1), f'Базовое HP должно быть от {MAX_BASE_HP} до {MAX_BASE_HP}'
        assert base_atack in range(MIN_BASE_ATACK, MAX_BASE_ATACK+1), f'Базовый урон должно быть от {MIN_BASE_ATACK} до {MAX_BASE_ATACK}'
        assert base_protection in range(MIN_BASE_PROTECTION, MAX_BASE_PROTECTION+1), f'Базовая защита должна быть от {MIN_BASE_PROTECTION} до {MAX_BASE_PROTECTION}'
        self.name = name
        self.hp = hp
        self.atack = base_atack
        self.protection = base_protection 
        self.precision = BASE_PRECISION
        self.crit = BASE_CRIT
        if self.__class__.__name__ == 'Person':
            print(f'На арене появился - {self.name}!')

    def take_on_cheracter_gear(self, set_things: List[Thing]):
        self.items = []
        print('НАДЕТЬ СНАЯРЖЕНИЕ!')
        print(f'____________________________')
        for thing in set_things:
            print(thing)
            self.items.append(thing.name)
            self.hp += thing.add_hp
            self.atack += thing.damage
            self.protection += thing.protection
            self.precision += thing.precision
            self.crit += thing.crit
            sleep(0.5)
        return (
            f'____________________________\n'
            f'ЭКИПИРОВКА ЗАКОНЧЕНА!\n\n'
            f'Экипированы: {" ,".join(self.items)}\n'
            f'Теперь у персонажа {self.name}:\n'
            f'HP = {self.hp}\n'
            f'Atack = {self.atack}\n'
            f'Protection = {self.protection}\n'
            f'Precision (меткость) = {self.precision}\n'
            f'Crit = {self.crit}\n'
        )
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}'

    def shoot(self, precision: int, damage: int) -> int:
        tmp = randint(MIN_PCT, MAX_PCT)
        if precision in range(MIN_PCT, tmp):
            return damage
        else:
            return 0

    def attack(self, enemy: 'Person') -> int:
        print(f'{self} атакует {enemy}!')
        damage = self.shoot(self.precision, self.atack) * (1 + (self.crit/MAX_PCT))
        enemy.take_damage(self, damage)

    def take_damage(self, enemy: 'Person', damage: int ) -> int:
        print(f'{enemy} бьет {self}! Входящий урон {damage}\n')
        tmp = 0
        if damage > 0:
            tmp = damage * (self.protection / 100)
        print(f'{self} получил {tmp} урона! АБСООООРБ!\n')
        self.hp -= tmp
        if self.hp < 1:
            print (f'У {self} осталось 0 HP\n')
        else:
            print (f'У {self} осталось {self.hp} HP\n')

    





