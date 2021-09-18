from classes import Paladin, Thing, Warrior
import random
from operator import attrgetter, itemgetter

PLAYERS_NUMBER = 10
THINGS_NUMBER = 20
FISRT_WORD_INPERSON = ['Великий', 'Могучий', 'Рожденный в СССР', 'Голосующий всегда ЗА!', 'Невысокого роста', 'Неприметный']
SECOND_WORD_INPERSON = ['рыцарь', 'воин', 'боец', 'крестоносец', 'гвардеец кардинала', 'закованный в железные доспехи']
NAME_INPERSON = ['Феофан', 'Олег', 'Стефан', 'Арни', 'Георг', 'Карл']
FISRT_INTHINGS = [
    {'стальной': [0.9, 1, 1]},
    {'ржавый': [0.5, 0.8, 0.8]},
    {'алмазный': [1, 1.5, 1.2]}
]
SECOND_INTHINGS = [
    {'щит': [0.1, 10, 100]},
    {'меч': [0.05, 100, 200]},
    {'лук': [.01, 70, 50]},
]

in_game = []


def in_game_players(x):
    for i in range(x):
        rnd_object = random.choice([Paladin, Warrior])
        in_game.append(
            rnd_object(
                f'{random.choice(FISRT_WORD_INPERSON)}'
                f' {random.choice(SECOND_WORD_INPERSON)}'
                f' {random.choice(NAME_INPERSON)}',
                random.randint(0, 50),
                random.randint(50, 100),
                random.randint(300, 500)
            )
        )
     

game_things = []


def in_game_things(x):
    for i in range(x):
        thing_material = random.choice(FISRT_INTHINGS)
        key_material = list(thing_material.keys())[0]
        thing_type = random.choice(SECOND_INTHINGS)
        key_type = list(thing_type.keys())[0]
        current_thing = Thing(
            f'{key_material} {key_type}',
            round(thing_material[key_material][0]*thing_type[key_type][0], 2),
            round(thing_material[key_material][1]*thing_type[key_type][1], 2),
            round(thing_material[key_material][2]*thing_type[key_type][2], 2),
            )
        game_things.append(current_thing)

in_game_players(PLAYERS_NUMBER)
in_game_things(THINGS_NUMBER)
game_things.sort(key=attrgetter('deffense') )    

def things_wearing():
    for i in range(PLAYERS_NUMBER):
        in_game[i].wearing(game_things[i])
    for i in range(PLAYERS_NUMBER,THINGS_NUMBER):
        rnd_person = random.randint(0, PLAYERS_NUMBER-1)
        if len(in_game[rnd_person].wear) < 4:
            in_game[rnd_person].wearing(game_things[i])

things_wearing()
