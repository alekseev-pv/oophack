from random import randint
from characters import Person


class Paladin(Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.hp = hp * 2
        self.protection = base_protection * 2
        self.resistance = 17
        print(f'Явился новый воин Альянса!\n   Дитя света -  {self}')

class Mage (Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.pinetra = 20
        self.resistance = 10
        print(f'Явился новый воин Альянса!\n   Дитя света -  {self}')
    def attack(self, enemy: 'Person'):
        print(f'{self} атакует {enemy}!')
        damage = int(self.atack * (1 + (self.crit/100)))
        enemy.take_damage(self, damage, mage_spell= True)

# Сделаю по мативам Вов классик))
# class Warrior(Person):
class Shaman(Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.atack = base_atack * 2
        self.crit += 10 
        self.resistance = 10
        self.pinetra = 5
        print(f'Явился новый воин Орды!\n   {self}  Сам Вождь благославил его на бой!')

class Warloc_pet():
    def __init__(self, owner: 'Warloc'):
        self.damage = int(owner.atack * (randint(30, 60)/100))
        self.owner = owner
    def attack(self):
        print(f'Петомен {self.owner}, атакукует, нанося {self.damage} урона')
        return self.damage
class Warloc(Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.pinetra = 20
        self.resistance = 10
        self.pet = Warloc_pet(self)
        print(f'Явился новый воин Орды!\n   {self}  Сам Вождь благославил его на бой!')
    def attack(self, enemy: 'Person'):
        print(f'{self} атакует {enemy}!')
        damage = int(self.atack * (1 + (self.crit/100)))
        enemy.take_damage(self, self.pet.attack())
        enemy.take_damage(self, damage, mage_spell=True)