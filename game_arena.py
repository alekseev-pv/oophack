import random

from heroes import Heroes
from my_classes import Paladin, Person, Warrior


all_heroes = []
arena = []
# Установим нужное количество героев для битвы
heroes_for_battle = Heroes(10)

for i in range(10):
    pattern = heroes_for_battle.make_a_pattern()
    hero = Person(pattern['name'], pattern['health_points'],
                  pattern['attack_points'], pattern['defence_points'])
    all_heroes.append(hero)

number_of_paladins = random.randint(0, 10)
number_of_warriors = 10 - number_of_paladins
print()
print(f"В битве примут участие паладинов - {number_of_paladins} "
      f" и воинов - {number_of_warriors}")
print()

for i in range(number_of_paladins):
    paladin = random.choice(all_heroes)
    all_heroes.remove(paladin)
    arena.append(Paladin(paladin.name, paladin.health_points,
                         paladin.attack_points, paladin.defence_points))


for warrior in all_heroes:
    arena.append(Warrior(warrior.name, warrior.health_points,
                         warrior.attack_points, warrior.defence_points))


# while len(arena) > 1:

player_1 = arena[0]
player_2 = arena[1]
print(f"На арену выходят {player_1.name} и {player_2.name}")
print(player_1)
print(player_2)
print()
print("Бойцы надевают экипирвку")
player_1 .get_equipment()
player_2.get_equipment()
print()
print("С учетом бонусов сила бойцов такова:")
player_1.set_things()
player_2.set_things()
print(player_1)
print(player_2)
print()
print("Бойцы готовы к бою")


battle_arena = []
first_strike = random.randint(0, 1)
battle_arena.append(arena.pop(first_strike))
battle_arena.append(arena[abs(first_strike - 1)])

player_1_limits = {'attack_bonuses': battle_arena[0].things[2]['life_time'],
                   'defence_bonuses': battle_arena[0].things[1]['life_time']}

player_2_limits = {'attack_bonuses': battle_arena[1].things[2]['life_time'],
                   'defence_bonuses': battle_arena[1].things[1]['life_time']}

limits = [player_1_limits, player_2_limits]

i = 2
continue_battle = True
while continue_battle:

    print()
    strike_index = i % 2
    defence_index = abs(i % 2 - 1)
    striking = battle_arena[strike_index]
    defending = battle_arena[defence_index]

    if limits[defence_index]['defence_bonuses'] == 0:
        defending.total_defence_points = defending.defence_points
        print(f"У {defending.name} пробита броня")

    print(f'{striking.name} наносит удар')
    continue_battle = defending.damage_count(battle_arena[i % 2])
    limits[strike_index]['attack_bonuses'] -= 1
    limits[defence_index]['defence_bonuses'] -= 1

    if limits[strike_index]['attack_bonuses'] == 0:
        striking.total_attack_points = striking.attack_points
        print(f"У {striking.name} кончились патроны")

    i += 1
print(defending.name)
