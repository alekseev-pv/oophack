from __future__ import annotations
import colorama
from colorama import Fore, Back, Style


colorama.init()

class Thing:
    def __init__(
        self,
        name: str,
        deffense: float,
        attack: float,
        health: float
    ) -> None:
        self.name = name
        self.deffense = deffense
        self.attack = attack
        self.health = health

    def about(self):
        print(f'{self.name}/{self.deffense}/{self.attack}/{self.health}')


class Person(Thing):
    def __init__(
        self,
        name: str,
        deffense: float,
        attack: float,
        health: float
    ) -> None:
        super().__init__(name, deffense, attack, health)
        self.wear = []
        self.final_prot = self.deffense / 100

    def wearing(self, thing: Thing):
        self.attack = self.attack + thing.attack
        self.final_prot = round(self.final_prot + thing.deffense,2)
        self.wear.append(thing.name)

    def status(self):
        print(f'Боец: {self.name}\nЗащита:{self.deffense}({self.final_prot})\tАтака:{self.attack}\t\tЖизни:{self.health}\tНа нем:{self.wear}')

    def get_damage(self, damage) -> float:
        self.health = round(self.health - damage, 2)
    
    def attacks(self, opponent: Person):
        self.damage = round(self.attack - self.attack * opponent.final_prot,2)
        print(Fore.RED + f'{self.name}' + Fore.WHITE + f' наносит удар по' + Fore.RED + f' {opponent.name}' + Fore.WHITE + ' на ' + Fore.BLUE + f'{self.damage}' + Fore.WHITE + ' урона')
        opponent.get_damage(self.damage)
        end_of_phrase = Fore.WHITE + 'у него ' + Fore.CYAN+ f'{opponent.health} hp' if opponent.health > 0 else Fore.RED + ' он RIP' 
        print (Fore.RED + f'{opponent.name}'+ Fore.WHITE +' потерял ' + Fore.RED + f'{self.damage}' + Fore.WHITE + ' жизней, и теперь' + f'{end_of_phrase}')
        print(Style.RESET_ALL)
       

class Paladin(Person):
    def __init__(self, name: str, deffense: float, attack: float, health: float) -> None:
        super().__init__(name, deffense, attack, health)
        self.deffense = self.deffense * 2
        

class Warrior(Person):
    def __init__(self, name: str, deffense: float, attack: float, health: float) -> None:
        super().__init__(name, deffense, attack, health)
        self.attack = self.attack * 2