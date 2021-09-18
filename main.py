from war import choice_class
from characters import Person
from classes import Paladin, Shaman
from war import fight, take_on_gear
from gear import Thing, parse_gear
import json
import os
import inspect
from random import choice, randint, random, sample

NAMES = [
    'Вариан Ринн', 'Тралл', 'Marc',
    'Orend','Kstorm','Jihann','Ngstopan',
    'Chlan','Wendonna','Windya','Naiyoshi',
    'Stynare','Tembe','Fissanna','Sannead',
    'Gwynell'
    ]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def sort_key(e):
    return e['precision']
if __name__ == '__main__':
    gears = os.path.join(BASE_DIR, "gear.json")
    with open(gears, "r") as read_file:
        gears = json.load(read_file)

    # отсортировали по возрастанию precision
    for a, b in gears.items():
        gears[a] = sorted(b, key=sort_key)

    gears_dict = parse_gear(gears)

    # Создаем список словарей с праметрами плееров
    players = []
    for i in range(0,10):
        name = choice(NAMES)
        NAMES.remove(name)
        hp = randint(20, 100)
        base_atack  = randint(2,15)
        base_protection  = randint(2,15)
        players.append(
            {
                'name': name,
                'hp': hp,
                'base_atack': base_atack,
                'base_protection': base_protection
            }
        )

    persones = []
    for player in players:
        #print(player)
        name, hp , base_atack, base_protection = player.values()
        tmp = Person(name, hp , base_atack, base_protection)
        rand = randint(1,2)
        if rand == 1:
            tmp = choice_class(tmp, Paladin)
        else:
            tmp = choice_class(tmp, Shaman)
        take_on_gear(tmp, gears_dict)
        persones.append(tmp)
    

    while True:
        players_fight = sample(persones, k=2)
        to_delete = fight(players_fight[0], players_fight[1])
        print(f'{to_delete} покидает турнир!')
        print(len(persones))
        persones.remove(to_delete)
        print(len(persones))
        if len(persones) == 1:
            print(f'Победил: {persones[0]}')
            break
    
    # human = Person(
    #     name='Вариан Ринн',
    #     hp=80,
    #     base_atack=10,
    #     base_protection=15
    #     )
    # human = choice_class(human, Paladin)
    # take_on_gear(human, gears_dict)
    # orc = Person(
    #     name='Тралл',
    #     hp=40,
    #     base_atack=15,
    #     base_protection=10
    #     )
    # orc = choice_class(orc, Shaman)
    # take_on_gear(orc, gears_dict)
    # fight(human, orc)