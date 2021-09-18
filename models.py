from __future__ import annotations

import random
import time

from assets import CHARACTERS, ITEMS


armory = []

class Item(object):
    def __init__(self, attack: float, defense: float, durability: int,
                 name: str) -> None:
        self.attack = attack / 100
        self.defense = defense / 100
        self.durability = durability
        self.name = name
        if self.defense > 0.1:
            self.defense = 0.1

    def __str__(self) -> str:
        item = {'name': self.name, 'defense': self.defense,
                'durability': self.durability, 'attack': self.attack}
        return item

    def show(self):
        print(f'Item name: {self.name}')
        print(f'attack: {self.attack}\ndefense: {self.defense}\n'
              f'durability: {self.durability}\n\n')


for item in ITEMS:
    item = Item(
        item['attack'],
        item['defense'],
        item['durability'],
        item['name'],
    )
    armory.append(item.__str__())

class Person(object):
    equipped_gear = ''

    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.name = name

    def __str__(self) -> str:
        hero = {'name': self.name, 'defense': self.defense,
                'hp': self.hp, 'attack': self.attack}
        return hero

    def show(self):
        print(f'{self.name} has entered the arena')
        print(
            f'Stats: {self.hp} hp, {self.attack} damage rate, {self.defense} defense.\n\n')

    def select_gear(self, gear: list = armory):
        i = random.randrange(len(armory))
        item = gear[i]
        self.equipped_gear = item['name']
        self.attack += (self.attack * item['attack'])
        self.defense += (self.defense * item['defense'])
        print(f'{self.name} is equipped with {self.equipped_gear}')

    def deal_damage(self) -> int:
        print(f'{self.name} deals {self.attack} damage with {self.equipped_gear}')
        return self.attack

    def take_damage(self, damage: int) -> None:
        self.hp = self.hp - damage
        print(f'{self.name} takes {damage} damage')
        print(f'Remaining hp: {self.hp}')


class Obsidian(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.hp = hp * 2
        self.defense = defense * 2


class Gold(Person):
    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        super().__init__(hp, attack, defense, name)
        self.attack = attack * 2


def define_fighter(fighter):
    if fighter['fraction'] == 'gold':
        player = Gold(
            fighter['hp'],
            fighter['attack'],
            fighter['defense'],
            fighter['name'])
    elif fighter['fraction'] == 'obsidian':
        player = Obsidian(
            fighter['hp'],
            fighter['attack'],
            fighter['defense'],
            fighter['name'])
    return player

def initiate_duel():
    first_pick = random.choice(CHARACTERS)
    second_pick = random.choice(CHARACTERS)
    first_fighter = define_fighter(first_pick)
    second_fighter = define_fighter(second_pick)

    first_fighter.select_gear()
    second_fighter.select_gear()


    while first_fighter.hp > 0 and second_fighter.hp > 0:
        hit = first_fighter.deal_damage()
        second_fighter.take_damage(hit)
        time.sleep(0.5)
        

initiate_duel()