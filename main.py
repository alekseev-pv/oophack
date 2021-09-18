from war import choice_class
from characters import Person
from classes import Paladin, Shaman
from war import fight, take_on_gear
from gear import Thing, parse_gear
import json
import os
import inspect
from colorama import Fore, Back, Style

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    gears = os.path.join(BASE_DIR, "gear.json")
    with open(gears, "r") as read_file:
        gears = json.load(read_file)
    #print(gears)
    gears_dict = parse_gear(gears)
    #print(gears_dict) 
    
    human = Person(
        name='Вариан Ринн',
        hp=80,
        base_atack=10,
        base_protection=15
        )
    human = choice_class(human, Paladin)
    take_on_gear(human, gears_dict)
    # orc = Person(
    #     name='Тралл',
    #     hp=60,
    #     base_atack=15,
    #     base_protection=10
    #     )
    # choice_class(orc, Shaman)
    #take_on_gear(orc, gears_dict)
    #fight(human, orc)