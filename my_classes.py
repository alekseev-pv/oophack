import random
from typing import Optional, Union

from weapon_and_armour import Armory


class Thing():
    '''Харрактеризует предмет.
    '''

    def __init__(self,
                 name: str,
                 defence_boost: float,
                 attack_boost: float,
                 life_boost: float,
                 life_time: float,
                 can_be_stolen: Optional[bool] = True) -> None:
        self.name = name,
        self.defence_boost = defence_boost
        self.attack_boost = attack_boost
        self.life_boost = life_boost
        self.life_time = life_time
        self.can_be_stolen = can_be_stolen


class Person():
    '''Харрактеризует персонаж.
    '''

    def __init__(self,
                 name: str,
                 health_points: float,
                 attack_points: float,
                 defence_points: float) -> None:
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.defence_points = defence_points
        self.total_health_points = health_points
        self.total_attack_points = attack_points
        self.total_defence_points = defence_points

        self.things = []

    def get_equipment(self):

        none_amount = 3
        armory_items = Armory().armory.keys()
        choises = ['none', 'min', 'mid', 'max', 'extra']
        for item in armory_items:
            choice = random.choice(choises)
            if choice == 'none':
                none_amount -= 1
                if none_amount == 0:
                    choises.remove('none')
            self.things.append(Armory().armory[item][choice])

    def set_things(self) -> None:

        life_boost = sum([thing['life_boost'] for thing in self.things])
        attack_boost = sum([thing['attack_boost'] for thing in self.things])
        defence_boost = sum([thing['defence_boost'] for thing in self.things])

        self.total_health_points = self.health_points + life_boost
        self.total_attack_points = self.attack_points + attack_boost
        self.total_defence_points = self.defence_points + defence_boost

    def damage_count(self, enemy) -> None:

        damage_recieved = round(enemy.total_attack_points - (
            enemy.total_attack_points * self.total_defence_points), 2)
        self.total_health_points -= damage_recieved
        if self.total_health_points <= 0:
            print(f"{self.name} умирает на арене от полученных ран")
            return False
        print(f"{self.name} получает урон {damage_recieved} и продолжает битву")
        return True

    def __str__(self):
        return(f"{self.name}: уровень жизни - {self.total_health_points}, "
               f"сила атаки - {self.total_attack_points}, мощность защиты - {self.total_defence_points}")


class Paladin(Person):

    def __init__(self,
                 name: str,
                 health_points: float,
                 attack_points: float,
                 defence_points: float) -> None:
        super().__init__(name, health_points, attack_points, defence_points)
        self.health_points *= 2
        self.defence_points *= 2


class Warrior(Person):

    def __init__(self,
                 name: str,
                 health_points: float,
                 attack_points: float,
                 defence_points: float,
                 death_blow: bool = True) -> None:
        super().__init__(name, health_points, attack_points, defence_points)
        self.attack_points *= 2
        self.defence_points = defence_points
        self.death_blow = death_blow


class Thief(Person):
    pass
