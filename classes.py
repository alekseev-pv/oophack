from random import randint
from characters import Person

# Надо играться с характеристиками классов...
# Но я старался))
class Paladin(Person):
    def __init__(self, name: str, hp: int, base_damage: int, base_protection: int):
        super().__init__(name, hp, base_damage, base_protection)
        self.hp = hp * 2
        self.protection = base_protection # * 2
        self.resistance = 10
        print(f'Явился новый воин Альянса!\n   Дитя света -  {self}')

class Mage (Person):
    def __init__(self, name: str, hp: int, base_damage: int, base_protection: int):
        super().__init__(name, hp, base_damage, base_protection)
        #self.protection = int(base_protection * 2)
        self.crit = 50
        self.pinetra = 20
        self.resistance = 10
        print(f'Явился новый воин Альянса!\n   Дитя света -  {self}')
    def attack(self, enemy: 'Person'):
        print(f'{self} атакует {enemy}!')
        damage = int(self.damage * (1 + (self.crit/100)))
        enemy.take_damage(self, damage, mage_spell= True)

# Сделаю по мативам Вов классик))
# class Warrior(Person):
class Shaman(Person):
    def __init__(self, name: str, hp: int, base_damage: int, base_protection: int):
        super().__init__(name, hp, base_damage, base_protection)
        self.damage = base_damage * 2
        self.crit += 30 
        self.resistance = 10
        self.pinetra = 5
        print(f'Явился новый воин Орды!\n   {self}  Сам Вождь благославил его на бой!')

class Warloc_pet():
    def __init__(self, owner: 'Warloc'):
        self.damage = int(owner.damage * (randint(30, 60)/100))
        self.owner = owner
    def attack(self):
        print(f'Петомен {self.owner}, атакукует, нанося {self.damage} урона')
        return self.damage
class Warloc(Person):
    def __init__(self, name: str, hp: int, base_damage: int, base_protection: int):
        super().__init__(name, hp, base_damage, base_protection)
        #self.protection = int(base_protection * 3)
        self.crit = 40
        self.pinetra = 20
        self.resistance = 10
        self.pet = Warloc_pet(self)
        print(f'Явился новый воин Орды!\n   {self}  Сам Вождь благославил его на бой!')
    def attack(self, enemy: 'Person'):
        print(f'{self} атакует {enemy}!')
        damage = int(self.damage * (1 + (self.crit/100)))
        enemy.take_damage(self, self.pet.attack())
        enemy.take_damage(self, damage, mage_spell=True)