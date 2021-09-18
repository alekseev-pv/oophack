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
    for item in names:
        armor_items[item] = Thing(item,randrange(0,200),None,randrange(0,200))
    return armor_items

def generate_weapons(names):
    weapon_items = {}
    for item in names:
        weapon_items[item] = Thing(item, None, randrange(0,300), randrange(0,100))
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

def equip_characters(characters, weapons, armors):
    while i:=0 < len(characters):
        char = characters[i]
        equip = generate_equip_list(weapons, armors)
        char.equip_item(equip)
        i+=1

equip_characters(characters, weapons, armors)
        




