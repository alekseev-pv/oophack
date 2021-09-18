class Person(object):
    """Прародитель персонажей"""

    def __init__(self, name, health, attack, defence):
         self.name = name
         self.health = health
         self.attack = attack
         self.defence = defence

    def set_things(self, things):
        print(f'{self.name} экипируется')
        for thing in things:
            self.equip_item(thing)

    def equip_item(self, item):
        print(f'{self.name} экипирует себе {item.name}')
        if item.attack_mod is not None:
            self.attack = self.attack+item.attack_mod
            print(f'Атака персонажа увеличивается на {item.attack_mod}')
        if item.defence_mod is not None:
            self.defence = self.defence + (self.defence*item.defence_mod)
            print(f'Защита персонажа увеличивается на {item.defence_mod} %')
        if item.health_mod is not None:
            self.health = self.health + item.health_mod
            print(f'Персонаж {self.name} ощущает рост жизненных сил на {item.health_mod}')

class Paladin(Person):
    """Класс рыцарь-паладин"""

    def __init__(self,name, health, attack, defence):
        super().__init__(name, health, attack, defence)
        self.health = health*2
        self.defence = defence*2
        print(f'Персонаж {self.name} класса паладин создан')
    
class Warrior(Person):
    """Класс Воин"""

    def __init__(self,name, health, attack, defence):
        super().__init__(name, health, attack, defence)
        self.attack = attack*2
        print(f'Персонаж {self.name} класса воин создан')
