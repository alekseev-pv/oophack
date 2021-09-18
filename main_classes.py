import random
import colorama
from colorama import Fore, Back, Style
from abc import ABC

colorama.init()


class Thing:
    def __init__(
            self,
            name,
            bonus_attack=0,
            bonus_defense=0,
            bonus_health=0,
            bonus_dodge=0,
            bonus_block=0,
            extra=None
    ):
        self.name = name
        self.bonus_attack = bonus_attack
        self.bonus_defense = bonus_defense
        self.bonus_health = bonus_health
        self.bonus_dodge = bonus_dodge
        self.bonus_block = bonus_block
        self.extra = extra


class Person(ABC):
    death_health = 0

    def __init__(self, name, damage=10, armor=10, dodge=15, block=30):
        self.name = name
        self.health = 100
        self.damage = damage
        self.armor = armor
        self.dodge = dodge
        self.block = block

    def hit(self, damage):
        if random.randint(0, 100) <= self.dodge:
            print(Fore.GREEN + f'{self.name} увернулся от удара')
            return None
        if random.randint(0, 100) <= self.block:
            print(Fore.BLUE + f'{self.name} заблокировал удар')
            return None
        strike_multiplier = (random.randint(50, 150) / 100)
        strike_power = round(damage * ((100 - self.armor) / 100) * strike_multiplier)
        print(Fore.RED + f'силой {strike_power}')
        self.health -= strike_power
        if self.health <= Person.death_health:
            print(Fore.LIGHTCYAN_EX + f'{self.name} не может продолжать бой')
        else:
            print(Fore.MAGENTA + f'У {self.name} осталось {self.health} единиц здоровья')
        return None

    def is_dead(self):
        if self.health <= Person.death_health:
            return f'{self.name} побежден!'


class Warrior(Person):
    def __init__(self, name, inventory):
        super().__init__(name)
        self.inventory = inventory
        self.bonus_damage = (sum(thing.bonus_attack for thing in inventory) + 100) / 100
        self.bonus_defense = (sum(thing.bonus_defense for thing in inventory) + 100) / 100
        self.bonus_health = (sum(thing.bonus_health for thing in inventory) + 100) / 100
        self.bonus_dodge = (sum(thing.bonus_dodge for thing in inventory) + 100) / 100
        self.bonus_block = (sum(thing.bonus_block for thing in inventory) + 100) / 100
        self.damage = self.damage * 2 * self.bonus_damage
        self.defense = self.armor * self.bonus_defense
        self.health = self.health * self.bonus_health
        self.dodge = self.dodge * self.bonus_dodge
        self.block = self.block * self.bonus_block
        self.name = name
        self.name_class = 'Воин'


class Paladin(Person):
    def __init__(self, name, inventory):
        super().__init__(name)
        self.inventory = inventory
        self.bonus_damage = (sum(thing.bonus_attack for thing in inventory) + 100) / 100
        self.bonus_defense = (sum(thing.bonus_defense for thing in inventory) + 100) / 100
        self.bonus_health = (sum(thing.bonus_health for thing in inventory) + 100) / 100
        self.bonus_dodge = (sum(thing.bonus_dodge for thing in inventory) + 100) / 100
        self.bonus_block = (sum(thing.bonus_block for thing in inventory) + 100) / 100
        self.damage = self.damage * self.bonus_damage
        self.defense = self.armor * 2 * self.bonus_defense
        self.health = self.health * 2 * self.bonus_health
        self.dodge = self.dodge * self.bonus_dodge
        self.block = self.block * self.bonus_block
        self.name = name
        self.name_class = 'Паладин'


class Rogue(Person):
    def __init__(self, name, inventory):
        super().__init__(name)
        self.inventory = inventory
        self.bonus_damage = (sum(thing.bonus_attack for thing in inventory) + 100) / 100
        self.bonus_defense = (sum(thing.bonus_defense for thing in inventory) + 100) / 100
        self.bonus_health = (sum(thing.bonus_health for thing in inventory) + 100) / 100
        self.bonus_dodge = (sum(thing.bonus_dodge for thing in inventory) + 100) / 100
        self.bonus_block = (sum(thing.bonus_block for thing in inventory) + 100) / 100
        self.damage = self.damage * 1.5 * self.bonus_damage
        self.defense = self.armor * self.bonus_defense
        self.health = self.health * 0.75 * self.bonus_health
        self.dodge = self.dodge * 3 * self.bonus_dodge
        self.block = self.block * self.bonus_block * 0
        self.name = name
        self.name_class = 'Разбойник'


class Crusader(Person):
    def __init__(self, name, inventory):
        super().__init__(name)
        self.inventory = inventory
        self.bonus_damage = (sum(thing.bonus_attack for thing in inventory) + 100) / 100
        self.bonus_defense = (sum(thing.bonus_defense for thing in inventory) + 100) / 100
        self.bonus_health = (sum(thing.bonus_health for thing in inventory) + 100) / 100
        self.bonus_dodge = (sum(thing.bonus_dodge for thing in inventory) + 100) / 100
        self.bonus_block = (sum(thing.bonus_block for thing in inventory) + 100) / 100
        self.damage = self.damage * 1.5 * self.bonus_damage
        self.defense = self.armor * self.bonus_defense
        self.health = self.health * 1.5 * self.bonus_health
        self.dodge = self.dodge * self.bonus_dodge
        self.block = self.block * self.bonus_block * 0
        self.name = name
        self.name_class = 'Крестоносец'

