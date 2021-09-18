from random import randint
from gear import Thing
from typing import List
from time import sleep

MIN_PCT = 1
MAX_PCT = 100
MIN_BASE_HP = 20
MAX_BASE_HP = 100
MAX_BASE_DAMAGE = MAX_BASE_PROTECTION = 15
MIN_BASE_DAMAGE = MIN_BASE_PROTECTION = 2
BASE_PRECISION = BASE_CRIT = 10
class Person:
    ''' Персонаж'''
    def __init__(
        self,
        name: str,
        hp: int,
        # Знаю, я тут напортачил что то с названием))
        base_damage: int,
        base_protection: int, 
    ):
        assert hp in range(MIN_BASE_HP, MAX_BASE_HP+1), f'Базовое HP должно быть от {MIN_BASE_HP} до {MAX_BASE_HP}, имеем {hp}'
        assert base_damage in range(MIN_BASE_DAMAGE, MAX_BASE_DAMAGE+1), f'Базовый урон должно быть от {MIN_BASE_DAMAGE} до {MAX_BASE_DAMAGE}'
        assert base_protection in range(MIN_BASE_PROTECTION, MAX_BASE_PROTECTION+1), f'Базовая защита должна быть от {MIN_BASE_PROTECTION} до {MAX_BASE_PROTECTION}'
        self.name = name
        self.hp = hp
        self.damage = base_damage
        self.protection = base_protection 
        self.precision = BASE_PRECISION
        self.crit = BASE_CRIT
        self.pinetra = 0
        self.resistance = 0
        if self.__class__.__name__ == 'Person':
            print(f'На арене появился - {self.name}!')

    def take_on_cheracter_gear(self, set_things: List[Thing]):
        self.items = []
        print('НАДЕТЬ СНАЯРЖЕНИЕ!')
        print(f'____________________________')
        for thing in set_things:
            #sleep(1)
            print(thing)
            self.items.append(thing.name)
            self.hp += thing.add_hp
            self.damage += thing.damage
            self.protection += thing.protection
            self.precision += thing.precision
            self.crit += thing.crit
            self.pinetra += thing.pinetra
            self.resistance += thing.resistanse
        return (
            f'____________________________\n'
            f'ЭКИПИРОВКА ЗАКОНЧЕНА!\n\n'
            f'Экипированы: {" ,".join(self.items)}\n'
            f'Теперь у персонажа {self.name}:\n'
            f'HP = {self.hp}\n'
            f'Atack = {self.damage}\n'
            f'Protection = {self.protection}\n'
            f'Precision (меткость) = {self.precision}\n'
            f'Crit = {self.crit}\n'
            f'Pinetra = {self.pinetra}\n'
            f'Resistance = {self.resistance}\n'
        )
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}'

    def shoot(self, precision: int, damage: int) -> int:
        tmp = randint(BASE_PRECISION, BASE_PRECISION*3)
        if precision >= tmp:
            return damage
        else:
            return 0

    def attack(self, enemy: 'Person'):
        print(f'{self} атакует {enemy}!')
        damage = int(self.shoot(self.precision, self.damage) * (1 + (self.crit/MAX_PCT)))
        enemy.take_damage(self, damage)

    def take_damage(self, enemy: 'Person', damage: int, mage_spell: bool = False):
        print(f'{enemy} бьет {self}! Входящий урон {damage}\n')
        tmp = 0
        if mage_spell:
            if self.resistance > enemy.pinetra:
                print(f'Как жаль, {enemy} не хватило пинетры ({enemy.pinetra})... у {self} - {self.resistance} ед сопротивления магическим заклинаниям.')
            else:
                tmp = damage
                print(f'{self} получил {tmp} урона! Это магический спэл, он не промахивается!')
        else:
            if damage > 0:
                tmp = int(damage * (1 - self.protection / 100))
                print(f'{self} получил {tmp} урона! АБСОРБ - {self.protection}%!\n')
            else:
                print(f'{enemy} промахнулся!')
        self.hp -= tmp
        if self.hp < 1:
            print (f'У {self} осталось 0 HP\n')
        else:
            print (f'У {self} осталось {self.hp} HP\n')

    





