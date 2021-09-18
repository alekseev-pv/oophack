from typing import List
from items import Thing
from colorama import Fore, Style


class Person:
    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = float(defense / 100)
        self.things: List[Thing] = []
        self.extra_hp = 0

    def _get_attack(self) -> int:
        total = self.attack
        total += sum(thing.attack for thing in self.things)

        return self.attack

    def set_things(self, things: List[Thing]) -> None:
        self.things.extend(things)
        self.extra_hp = sum(thing.hp for thing in self.things)

    def get_protection(self) -> float:
        total = self.defense
        total += sum(thing.defense for thing in self.things)

        # ограничиваем общую сумму защиты до 50%
        total = (int(total * 100) % 50) / 100
        return total

    def receive_attack(self, enemy: "Person") -> None:
        damage = int(
            enemy._get_attack() - (self.get_protection() * enemy._get_attack())
        )

        if self.extra_hp > 0:
            self.extra_hp -= damage
        elif self.extra_hp < 0:
            self.hp -= damage + abs(self.extra_hp)
            self.extra_hp = 0
        else:
            self.hp -= damage

        total_hp = self.hp + self.extra_hp
        print(
            f"{enemy.name} наносит удар по {self.name}"
            + Fore.RED
            + f" на {damage} урона"
            + Style.RESET_ALL
        )
        print(
            f"У {self.name}"
            + Fore.RED
            + f" осталось {total_hp}"
            + Style.RESET_ALL
        )


class Paladin(Person):
    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        super().__init__(name, hp * 2, attack, defense * 2)


class Warrior(Person):
    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        super().__init__(name, hp, attack * 2, defense)
