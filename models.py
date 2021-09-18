"""
Модуль описания моделей вещей (Thing)
и персонажей (Person) в игре.
"""

from typing import Optional, List
from abc import ABC, abstractclassmethod

class Thing:
    """
    Класс Вещи

    Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь.
    """
    def __init__(self,
                 name: str,
                 health_points: float,
                 defence: float,
                 attack_damage: float) -> None:
        self.name = name
        self.health_points = health_points
        self.defence = defence
        self.attack_damage = attack_damage
        
    
class Person:
    """
    Класс Персонажи

    Класс, содержащий в себе следующие параметры: 
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    """
    def __init__(self,
                 name: str,
                 health_points: float,
                 base_defence: float,
                 base_attack_damage: float) -> None:
        self.name = name
        self.health_points = health_points
        self.base_defence = base_defence
        self.base_attack_damage = base_attack_damage
        
        self.put_things = []
        
        self.summ_hp = health_points
        self.summ_def = base_defence
        self.summ_attack = base_attack_damage

    def set_things(self, things: List[Thing]) -> None:
        """
        Метод устанавливающий список вещей, надетых на персонажа.
        """
        self.put_things.extend(things)

    def taking_damage(self, damage: float) -> None:
        self.life -= damage


class Paladin(Person):
    """
    Класс Паладин

    Класс, описывающий персонажей типа Паладин
    (жизнь и защита удваиваются относительно базовых показателей).
    """
    def __init__(self,
                 name: str,
                 health_points: float,
                 base_defence: float,
                 base_attack_damage: float) -> None:
        super.__init__(self,
                       name,
                       health_points*2,
                       base_defence*2,
                       base_attack_damage)


class Warrior(Person):
    """
    Класс Воин

    Класс, описывающий персонажей типа Воин
    (базовая атака удваивается).
    """
    def __init__(self,
                 name: str,
                 health_points: float,
                 base_defence: float,
                 base_attack_damage: float) -> None:
        super.__init__(self,
                       name,
                       health_points,
                       base_defence,
                       base_attack_damage*2)