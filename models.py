"""
Модуль описания моделей вещей (Thing)
и персонажей (Person) в игре.
"""

from typing import List

from colorama import Fore, Style


class Thing:
    """
    Класс Вещи

    Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь.
    """
    def __init__(self,
                 name: str,
                 hitpoints: float,
                 protection: float,
                 attack_damage: float) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.protection = protection
        self.attack_damage = attack_damage

    def __str__(self) -> str:
        return ("\n" + Fore.YELLOW + "Thing:\n"
                f"Name - {self.name:.1f}\n"
                f"Health points - {self.hitpoints:.1f}\n"
                f"protection - {self.protection:.1f}\n"
                f"Attack attack_damage - {self.attack_damage:.1f}\n"
                + Style.RESET_ALL)


class Person:
    """
    Класс Персонажи

    Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    """
    def __init__(self,
                 name: str,
                 hitpoints: float,
                 base_protection: float,
                 base_attack_damage: float) -> None:
        self.name = name
        self.base_hitpoints = hitpoints
        self.base_protection = base_protection
        self.base_attack_damage = base_attack_damage

        self.things: List[Thing] = []

        self.final_hp = hitpoints
        self.final_protection = base_protection
        self.final_attack_damage = base_attack_damage

    def can_fight(self) -> bool:
        if self.final_hp <= 0:
            return False
        return True

    def damage_reduction(self, attack_damage: float) -> float:
        return attack_damage * (1 - self.final_protection)

    def set_things(self, things: List[Thing]) -> None:
        """
        Метод устанавливающий список вещей, надетых на персонажа.
        """
        self.things.extend(things)
        self.__put_on()

    def taking_attack_damage(self, attack_damage: float) -> None:
        self.final_hp -= self.damage_reduction(attack_damage)

    def __put_on(self) -> None:
        for thing in self.things:
            self.final_hp += thing.hitpoints
            self.final_protection += thing.protection
            self.final_attack_damage += thing.attack_damage

    def __str__(self) -> str:
        return (Fore.CYAN + f"Name - {self.name.upper()}\n"
                "BASE\n"
                f"\tBase Health - {self.base_hitpoints:.1f}\n"
                f"\tBase protection - {self.base_protection:.1f}\n"
                "\tBase Attack attack_damage"
                f" - {self.base_attack_damage:.1f}\n"
                "WITHS THING ["
                ", ".join([thing.name for thing in self.things]) +
                f"]\n\tHealth- {self.final_hp:.1f}\n"
                f"\tprotection- {self.final_protection:.2f}\n"
                f"\tAttack- {self.final_attack_damage:.1f}\n"
                + Style.RESET_ALL)


class Paladin(Person):
    """
    Класс Паладин

    Класс, описывающий персонажей типа Паладин
    (жизнь и защита удваиваются относительно базовых показателей).
    """
    def __init__(self,
                 name: str,
                 hitpoints: float,
                 base_protection: float,
                 base_attack_damage: float) -> None:
        super().__init__(name,
                         hitpoints*2,
                         base_protection*2,
                         base_attack_damage)
        self.type_hero = "Paladin"

    def print_statistic(self) -> None:
        print(f"Name - {self.name}")
        print(f"Type of hero - {self.type_hero}")
        print(f"Last HP - {self.final_hp:.1f}")
        print(f"Armor - {self.final_protection:.1f}")
        print(f"Attack damage - {self.final_attack_damage:.1f}")

    def __str__(self) -> str:
        return (Fore.CYAN + "Type of Hero - " +
                str(self.type_hero) + "\n" + super().__str__())


class Warrior(Person):
    """
    Класс Воин

    Класс, описывающий персонажей типа Воин
    (базовая атака удваивается).
    """
    def __init__(self,
                 name: str,
                 hitpoints: float,
                 base_protection: float,
                 base_attack_damage: float) -> None:
        super().__init__(name,
                         hitpoints,
                         base_protection,
                         base_attack_damage*2)
        self.type_hero = "Warrior"

    def print_statistic(self) -> None:
        print(f"Name - {self.name}")
        print(f"Type of hero - {self.type_hero}")
        print(f"Last HP - {self.final_hp:.1f}")
        print(f"Armor - {self.final_protection:.1f}")
        print(f"Attack damage - {self.final_attack_damage:.1f}")

    def __str__(self) -> str:
        return (Fore.CYAN + "Type of Hero - " +
                str(self.type_hero) + "\n" + super().__str__())
