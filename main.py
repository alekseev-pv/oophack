from random import choice, randrange

from characters import Paladin, Warrior
from strings import armor_names, character_names, weapon_names
from things import Thing


def generate_characters(names):
    characters = {}
    i = 0
    warrior_count = randrange(20)
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

def char_wear(characters,weapons, armors):
    i = 0
    while i < len(characters):
        items = generate_equip_list(weapons, armors)
        characters[i].set_things(items)
        i+=1

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
        
def mass_fight(characters):
    active = list(characters.values())
    while len(active)>1:
        player_one_idx = randrange(0,len(active))
        player_one = active[player_one_idx]
        print(f'В левом углу арены {player_one.name}')
        active.remove(player_one)
        player_two_idx = randrange(0,len(active))
        player_two = active[player_two_idx]
        print(f'в правом углу арены {player_two.name}')
        active.remove(player_two)
        winner = fight(player_one, player_two)
        print(f'Победитель схватки {winner.name}')
        active.append(winner)
    print(f'Чемпион вселенной {active[0].name}')

if __name__ == "__main__":
    generated_characters = generate_characters(character_names)
    generated_weapons = generate_weapons(weapon_names)
    generated_armors = generate_armor(armor_names)
    char_wear(generated_characters,generated_weapons,generated_armors)
    mass_fight(generated_characters)
