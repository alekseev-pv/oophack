from calendar import c
from random import randrange, choice

from characters import Paladin, Warrior
from things import Thing

character_names = ('Джон Коннор', 'Люк Скайуокер', 'Ганнибал Лектер',
    'Джек Торранс', 'Джокер', 'Норман Бейтс', 'Бэтмен', 'Зорро',
    'Эллен Рипли', 'Хан Соло', 'Оби-Ван Кеноби', 'Круэлла Де Виль',
    'Чужой', 'Хищник', 'Моисей', 'Фредди Крюгер', 'Дракула', 'Франкенштейн',
    'Доктор Браун', 'Джонни Рико', 'Терминатор', 'SHODAN', 'Рик Декард',
    'Пол Атрейдес', 'Владимир Харконнен', 'Грегор Эйхзенхорн', 'Император человечества')

weapon_names = ('Лазерный меч', 'Рельсовая Пушка', 'BFG', 'Пусьынный орёл',
'Катана', 'Железные Кулаки', 'MG42', 'Сила мысли', '7,2-дюймовая гаубица', 'Миномёт',
'Каменный топор', 'Гарпун', 'Бритва Мерунеса')

armor_names = ('Керамическая броня', 'Рыцарские латы', 'Лазерная броня', 'Силовая броня',
'Бронежилет', 'Пуховая подушка', 'Мантия невидимки', 'Маска Клавикуса Вайла', 'Эбонитовая Кольчуга ',
'Клёпаная броня', 'Драконья чешуя')



def generate_character(names):
    characters = {}
    i = 0
    warrior_count = randrange(15)
    while i < warrior_count:
        name = choice(names)
        characters[i] = Warrior(name,randrange(0,300), randrange(0,300), randrange(0,300))
        i += 1
    while i < 20:
        name = choice(names)
        characters[i] = Paladin(name,randrange(0,300), randrange(0,300), randrange(0,300))
        i += 1
    return characters
    
def generate_armor(names):
    armor_items = {}
    i = 0
    for item in names:
        armor_items[i] = Thing(item,(randrange(1,100)/1000),None,randrange(0,1000))
        i+=1
    return armor_items

def generate_weapons(names):
    weapon_items = {}
    i = 0
    for item in names:
        weapon_items[i] = Thing(item, None, randrange(0,100)/1000, randrange(0,1000))
        i+=1
    return weapon_items


def generate_equip_list(weapons, armors):
    items = []
    i = 0
    while i <= randrange(0,2):
        item_key = randrange(0,len(armors))
        items.append(armors[item_key])
        i += 1
    i = 0
    while i <= randrange(0,2):
        item_key = randrange(0,len(weapons))
        items.append(weapons[item_key])
        i += 1
    return items


characters = generate_character(character_names)
weapons = generate_weapons(weapon_names)
armors = generate_armor(armor_names)

def char_wear(characters,weapons, armors):
    i = 0
    while i < len(characters):
        items = generate_equip_list(weapons, armors)
        characters[i].set_things(items)
        i+=1

char_wear(characters,weapons,armors)

def fight(player_one, player_two):
    player_one_health = player_one.health
    player_two_health = player_two.health
    player_one_attack = player_one.attack
    player_two_attack = player_two.attack
    player_one_defence = player_one.defence
    player_two_defence = player_two.defence
    while player_one_health >= 0 or player_two_health >= 0:
        hit = player_one_attack-(player_one_attack*(player_two_defence/1000))
        print(f'{player_two.name} наносит удар по {player_one.name} на {hit} урона')
        player_two_health += -(hit)
        if player_two_health <= 0:
           return player_one
        hit = player_two_attack-(player_two_attack*(player_one_defence/1000))
        print(f'{player_one.name} наносит удар по {player_two.name} на {hit} урона')
        player_one_health += -(hit)
        if player_one_health <=0:
           return player_two
        

print(fight(characters[1],characters[2]))