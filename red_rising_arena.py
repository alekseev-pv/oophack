from __future__ import annotations


class Person(object):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.name = name

    def show(self):
        print(f'{self.name} has entered the arena')
        print(
            f'Stats: {self.hp} hp, {self.attack} damage rate, {self.defense} defense.')


class Obsidian(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.hp = hp * 2
        self.defense = defense * 2


class Gold(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.attack = attack * 2


darrow = Gold(100, 75, 50, 'Darrow')
darrow.show()