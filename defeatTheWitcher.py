from random import randint
from colorama import init, Fore, Back


from battle import LIST_BATTLE
from characters import LIST_CHARACTERS
from thing import LIST_THING


init(autoreset=True)
MESS_VIN = 'Победилем в схватке вышел {}!'
MESS_INPUT = ('Выберите, какое сражение хотите посетить:\n'
              '1.{}\n'
              '2.{}\n'
              '3.{}\n'
              '4.{}\n')
MESS_ERR = 'Некорректное значение.'
MESS_BATTLE_1 = 'На {}а напал {}!'
MESS_BATTLE_2 = '{} взял:'
MESS_BATTLE_3 = 'у {}а был:'
MESS_BATTLE_4 = 'Битва закончена, остался только {}.'


class Thing:
    def __init__(self, list_thing: dict):
        self.thing_name = list_thing.get('thing_name')
        self.thing_protection = list_thing.get('thing_protection')
        self.thing_attack = list_thing.get('thing_attack')
        self.thing_hit_points = list_thing.get('thing_hit_points')
        print(f'{self.thing_name}')


class Person:
    person_hit_points = 0.5
    person_protection = 0.1
    person_attack = 0.01

    def __init__(self,  characters):
        self.person_name = characters

    def set_things(self, thing_quantity):
        thing_choice_list = randomaizer(thing_quantity, LIST_THING)
        for thing_num in range(0, thing_quantity):
            thing = Thing(LIST_THING[thing_choice_list[thing_num]])
            self.person_protection = (self.person_protection
                                      + thing.thing_protection)
            self.person_attack = (self.person_attack
                                  + thing.thing_attack)
            self.person_hit_points = (self.person_hit_points
                                      + thing.thing_hit_points)

    def subtracting_health(self, attack_damage, characters):
        finalProtection = characters.person_protection
        self.person_protection = finalProtection-(
            attack_damage - attack_damage * finalProtection)
        if finalProtection < 0:
            self.person_hit_points = self.person_hit_points - attack_damage

    def attack_damage(self, characters):
        return characters.person_attack


class Paladin(Person):
    Person.person_hit_points = Person.person_hit_points * 2
    Person.person_protection = Person.person_protection * 2


class Warrior(Person):
    Person.person_attack = Person.person_attack * 2


def result_battle(person, warrior, list_vin):
    if person.person_protection < 0 or person.person_hit_points < 0:
        list_vin.remove(person.person_name)
        return MESS_VIN.format(warrior.person_name)
    list_vin.remove(warrior.person_name)
    return MESS_VIN.format(person.person_name)


def randomaizer(quantity, list_quantity):
    choice_list = []
    while len(choice_list)-1 != quantity:
        choice = randint(0, len(list_quantity)-1)
        if choice not in choice_list:
            choice_list.append(choice)
    return(choice_list)


def var_battle():
    name_battle = input(MESS_INPUT.format(
          LIST_BATTLE[0]["name_battle"],
          LIST_BATTLE[1]["name_battle"],
          LIST_BATTLE[2]["name_battle"],
          LIST_BATTLE[3]["name_battle"]))
    if int(name_battle)-1 not in range(len(LIST_BATTLE)):
        raise ValueError(MESS_ERR)
    return int(name_battle)-1


def battle():
    name_battle = var_battle()
    print(Fore.RED + LIST_BATTLE[name_battle]['description'])
    list_vin = LIST_CHARACTERS
    while len(list_vin) != 1:
        paladin = Paladin(list_vin[0])
        warrior = Warrior(list_vin[1])
        if len(list_vin) > 2:
            list_quantily = randomaizer(2, list_vin)
            paladin = Paladin(list_vin[list_quantily[0]])
            warrior = Warrior(list_vin[list_quantily[1]])
        print(MESS_BATTLE_1.format(paladin.person_name, warrior.person_name))
        print(MESS_BATTLE_2.format(paladin.person_name))
        paladin.set_things(randint(1, 4))
        print(MESS_BATTLE_3.format(warrior.person_name))
        warrior.set_things(randint(1, 4))
        paladin_person_hit_points = paladin.person_hit_points
        warrior_person_hit_points = warrior.person_hit_points
        while (paladin_person_hit_points > 0
               and warrior_person_hit_points > 0):
            paladin.subtracting_health(
                warrior.attack_damage(warrior),
                paladin)
            warrior.subtracting_health(
                warrior.attack_damage(paladin),
                warrior)
            paladin_person_hit_points = paladin.person_hit_points
            warrior_person_hit_points = warrior.person_hit_points
        print(
            Back.GREEN +
            Fore.RED +
            result_battle(paladin, warrior, list_vin))
    print(Fore.RED + Back.WHITE + MESS_BATTLE_4.format(list_vin[0]))


battle()
