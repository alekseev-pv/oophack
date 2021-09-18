from __future__ import annotations
from models import CHARACTERS, ITEMS
import random


class Person(object):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.name = name

    def show(self):
        print(f'{self.name} has entered the arena')
        print(
            f'Stats: {self.hp} hp, {self.attack} damage rate, {self.defense} defense.\n\n')


class Item(object):
    def __init__(self, attack: float, defense: float, durability: int,
                 name: str) -> None:
        self.attack = attack / 100
        self.defense = defense / 100
        self.durability = durability
        self.name = name
        if self.defense > 0.1:
            self.defense = 0.1
    
    def show(self):
        print(f'Item name: {self.name}')
        print(f'attack: {self.attack}\ndefense: {self.defense}\n'
              f'durability: {self.durability}\n\n')


class Obsidian(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.hp = hp * 2
        self.defense = defense * 2


class Gold(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.attack = attack * 2


for person in CHARACTERS:
    if person['fraction'] == 'gold':
        gold = Gold(
            person['hp'],
            person['attack'],
            person['defense'],
            person['name'])
        gold.show()
    else:
        obsidian = Obsidian(
            person['hp'],
            person['attack'],
            person['defense'],
            person['name'])
        obsidian.show()

for item in ITEMS:
    item = Item(
        item['attack'],
        item['defense'],
        item['durability'],
        item['name'],
    )
    item.show()