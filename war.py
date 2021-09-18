from characters import Person
from random import shuffle, randint

def fight(player_1: Person, player_2: Person, rounds: int = 1):
    
    # Кто атакует первый?
    all_fights = []
    for _ in range(rounds):
        one_attacks_two = (player_1, player_2)
        two_attacks_one = (player_2, player_1)
        fights = [one_attacks_two, two_attacks_one]
        shuffle(fights)
        all_fights.append(fights[0])
    print(all_fights)


    for count, pair in enumerate(all_fights, start=1):
        print(f'ROUND {count}! FIGHT!')
        #print(pair)
        attacker, victim = pair
        #print(attacker)
        while True:
            attacker.attack(victim)
            print()
            print(f'Принт из мэин{victim.hp}')
            if victim.hp <= 0:
                print(f'{attacker} WINS!')
                break

            victim.attack(attacker)
            print()

            if attacker.hp <= 0:
                print(f'{victim} WINS!')
                break