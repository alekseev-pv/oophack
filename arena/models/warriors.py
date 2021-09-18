from colorama import init
from termcolor import colored

init()


class Person():
    def __init__(self, name, defense, attack, health, sex):
        if defense > 0.5 or defense < 0:
            raise ValueError('Неверное значение защиты')
        if attack > 20 or attack < 0:
            raise ValueError('Неверное значение атаки')
        if health > 50 or health <= 0:
            raise ValueError('Неверное значение здоровья')
        self.name = str(name)
        self.defense = float(defense)
        self.attack = float(attack)
        self.health = float(health)
        if sex == 'W':
            self.sex = 'w'
        else:
            self.sex = 'm'
        self.things = []

    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack

    def finalDefense(self,):
        for thing in self.things:
            self.defense += thing.defense

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health

    def set_things(self, things):
        self.things.extend(things)
        self.finalAttack()
        self.finalDefense()
        self.finalHealth()

    def decrease_helth(self, attack_damage):
        damage = attack_damage - attack_damage * self.defense
        self.health -= damage
        print(colored(f'{self.name} получил урон - {damage}', 'red'))
        if self.health > 0:
            print(colored(f'Осталось {self.health} HP', 'blue'))
        else:
            print(colored(f'Боец {self.name} умер!', 'blue'))


class Paladin(Person):
    def finalDefense(self):
        for thing in self.things:
            self.defense += thing.defense
        self.defense *= 2

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health
        self.health *= 2


class Warrior(Person):
    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack
        self.attack *= 2


class Child(Paladin, Warrior):
    def __init__(self, name, defense, attack, health, sex):
        self.name = str(name)
        self.defense = float(defense)
        self.attack = float(attack)
        self.health = float(health)
        self.sex = sex
