from classes import Paladin, Shaman
from war import fight
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    gear = os.path.join(BASE_DIR, "gear.json")
    with open(gear, "r") as read_file:
        gear = json.load(read_file)
    #print(type(gear))
    human = Paladin(
        name='Вариан Ринн',
        hp=100,
        base_atack=10,
        base_protection=15
        )
    orc = Shaman(
        name='Тралл',
        hp=90,
        base_atack=15,
        base_protection=10
        )
    
    fight(human, orc)