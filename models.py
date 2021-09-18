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
    duelists = []
    equipped_gear = ''

    def __init__(self, hp: int, attack: int, defense: int, name: str) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.name = name
        __class__.duelists.append(self)

    def __str__(self) -> str:
        hero = {'name': self.name, 'defense': self.defense,
                'hp': self.hp, 'attack': self.attack}
        return hero

    def show(self):
        print(f'{self.name} has entered the arena!')
        print(
            f'Stats: {self.hp} hp, {self.attack} damage rate, {self.defense} defense.')
        if self.name == 'Darrow O\'Lykos':
            print('\nI am the Reaper and death is my shadow.')

    def select_gear(self, gear: list = armory):
        i = random.randrange(len(armory))
        item = gear[i]
        self.equipped_gear = item['name']
        self.attack += (self.attack * item['attack'])
        self.defense += (self.defense * item['defense'])
        self.show()
        print(f'{self.name} is equipped with {self.equipped_gear}\n')

    def deal_damage(self) -> int:
        print(f'{self.name} deals {self.attack} damage.\n')
        return self.attack

    def take_damage(self, damage: int) -> None:
        self.hp = self.hp - damage
        if self.hp > 0 and damage < self.hp:
            print(f'{self.name} takes {damage} damage')
            print(f'Remaining hp: {self.hp}\n')
        else:
            print(f'{self.name} has lost the duel!')
            print('Funny thing, watching gods realize they’ve been mortal all along.')


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
    time.sleep(2)
    second_fighter.select_gear()
    time.sleep(2)

    action = 0

    while first_fighter.hp > 0 and second_fighter.hp > 0:
        if action == 0:
            hit = first_fighter.deal_damage()
            second_fighter.take_damage(hit)
        elif action == 1:
            hit = second_fighter.deal_damage()
            first_fighter.take_damage(hit)
        action = random.randint(0, 1)
        time.sleep(1)


initiate_duel()
