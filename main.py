from random import sample, choice, uniform, randint

from tabulate import tabulate

from config import MAX_HP, NUMBER_PLAYERS
from characters import all_player_names, CHARACTER_CLASSES
from things import Thing, all_things




print('...звучит музыка...')
print('Что наша жизнь? ИГРА!')
print()
print('*'*50)

players = []
player_names = sample(all_player_names, NUMBER_PLAYERS)
for name in player_names:
    player_class = choice(CHARACTER_CLASSES)
    player = player_class(
        name = name,
        damage = uniform(0.05, 0.25) * MAX_HP,
        protection = uniform(0.25, 1) * 0.25,
        health_point = uniform(0.25, 1) * MAX_HP
    )
    player_things = sample(all_things, randint(1, 4))
    player.set_things(player_things)
    players.append(player)


print('За столом cегодня играют:')
print()

for player in players:
    player_things = ', '.join([thing.title for thing in player.things])
    print(f'Обладатель {player_things}')
    print(f'{player.name}.')
    print(f'(Атака {player.damage:.0f}, Защита {player.protection:.2f}, Здоровье {player.health_point:.0f}, {player.class_name})')
    print()
    print('*'*50)

graveyard = []

for game_round in range(1, NUMBER_PLAYERS):
    print('Играем до последнего знатока')
    print(f'Счет 0 : {NUMBER_PLAYERS - len(players)}')
    print(f'{game_round} раунд!')
    print()

    while True:
        attacker, defender = sample(players, 2)
        attack_damage = attacker.attack(defender)
        print(f'{attacker.name} атакует {defender.name}'
            f' и наносит ему {attack_damage:.0f} урона.'
        )
        if defender.is_alive:
            print(f'{defender.name} выживает на {defender.health_point:.0f} хп.')
        else:
            graveyard.append(defender)
            players.remove(defender)
            print(f'К сожалению, {defender.name} не выдерживает и "покидает наш стол"')
            break
        print()
    print()
    print('*'*50)
    print()
last_man_standing = players.pop()
graveyard.append(last_man_standing)
print('Сегодняшний победитель, единственный кто удержался за столом')
print()
print(f'{last_man_standing.name.upper()}')
print()
print('Звучит песня Тамары Гвердцители - Виват король')
print()


headers = ['Место','Игрок', 'Атака', 'Защита', 'Здоровье', 'Урон нанесено', 'Урон полученно', 'Класс']
game_result = []
place = 0
for player in reversed(graveyard):
    place += 1
    game_result.append([
        place,
        player.name,
        round(player.damage),
        round(player.protection, 2),
        round(player.init_health_point),
        round(player.damage_dealt),
        round(player.damage_taken),
        player.class_name,
        # ', '.join(thing.title for thing in player.things)
    ])

print(tabulate(game_result, headers, tablefmt="grid"))
