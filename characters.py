class Person:

    def __init__(self, name, base_attack, base_deff, base_hp):
        self.name = name
        self.base_deff = base_deff
        self.base_attack = base_attack
        self.base_hp = base_hp

    def __str__(self):
        return self.name

    def set_things(self, things):
        for thing in things:
            self.equip_thing(thing)

    def equip_thing(self, item):
        print(f'{self.name} получил {item.thing_name}')
        if item.t_attack is not None:
            self.base_attack = self.base_attack + item.t_attack
        if item.t_deff is not None:
            self.base_deff = self.base_deff + item.t_deff
        if item.t_hp is not None:
            self.base_hp = self.base_hp + item.t_hp
            print(f'Боец {self.name} получает бонусы:'
                  f'|Атака:+{item.t_attack}| |Защита:+{item.t_deff}|'
                  f' |Хп:+{item.t_hp}|')


class Paladin(Person):

    def __init__(self, name, base_attack, base_deff, base_hp):
        super().__init__(name, base_attack, base_deff, base_hp)
        self.base_hp = base_hp * 2
        self.base_deff = base_deff * 2
        print(f'Боец {self.name} из ордена паладинов прибыл.')


class Warrior(Person):

    def __init__(self, name, base_attack, base_deff, base_hp):
        super().__init__(name, base_attack, base_deff, base_hp)
        self.base_attack = base_attack * 2
        print(f'Боец {self.name} из касты войнов прибыл.')
