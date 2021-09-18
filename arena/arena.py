import random

from colorama import init
from models.things import Thing, sort_key
from models.warriors import Child, Paladin, Warrior
from termcolor import colored

init()
print(colored('\n\n_____ START GAME  _____\n\n', 'yellow'))

SURVIVAL = False

COUNT_THINGS_ON_PERS = 4

COUNT_PERSES = 10

NAMES = [
    'Keith Lowe',
    'Gary Palmer',
    'Lucille Carroll',
    'Joanne Baker',
    'Ruby Hill',
    'Douglas Perez',
    'Marjorie Hoffman',
    'Ashley Anderson',
    'Sarah Tyler',
    'Jennifer Turner',
    'Eric Jones',
    'Ivan Rodriguez',
    'Jesse Kim',
    'Stephen Wagner',
    'Leonard Stevenson',
    'Cathy Bennett',
    'Cathy Parker',
    'Brenda Pearson',
    'Thomas Ross',
    'Henry Watkins',
]

THINGS = sorted([
    Thing('Socks of Fortune', random.randint(0, 10) / 100,
          random.randint(0, 10), random.randint(0, 100)),
    Thing('Gods armor', 0.1, 0, 10),
    Thing('killing rage', 0, 10, 0),
    Thing('Ring of Health', 0, 0, 10),
    Thing('Ring of Power', 0.02, 5, 0),
    Thing('Casual hat', 0.1, 5, 5),
    Thing('Ferrobots', 0.1, 2, 3)
], key=sort_key)


def rand():
    klasse = Warrior if random.randint(0, 1) else Paladin
    name = NAMES.pop(random.randint(0, len(NAMES) - 1))
    defense = random.randint(0, 50) / 100
    attack = random.randint(0, 20)
    helth = random.randint(1, 20)
    sex = 'm' if random.randint(0, 1) else 'w'
    return klasse(name, defense, attack, helth, sex)


FIGHTERS = [rand() for _ in range(COUNT_PERSES)]


def create_person(klasse):
    gamer = klasse(
        name=input('Введите имя: '),
        defense=float(input('Установите защиту от 0 до 0.5:  ')),
        attack=float(input('Установите атаку от 0 до 20:  ')),
        health=float(input('Установите злоровье от 0 до 50:  ')),
        sex=(input('Выберит пол персонажа W/M:  ').upper()), )
    FIGHTERS.append(gamer)


def user_input():
    global SURVIVAL

    while True:
        gamer = input('Желаете создать нового персонажа? Y/N: ').upper()
        if gamer == 'Y':
            gamer = input('Выберите класс Warrior или Paladin - W/P: ').upper()
            if gamer == 'W':
                create_person(Warrior)
            elif gamer == 'P':
                create_person(Paladin)
            else:
                print('Вы не выбрали нужный класс, продолжим без Вас.')
        else:
            break
    survival = input('Хотите установить режим "На выживание"?'
                     ' Тогда бойцы не восстановят здоровье после боя: Y/N: '
                     ).upper()
    SURVIVAL = survival == 'Y'


def get_things(fighters, things):
    for fighter in fighters:
        limit = random.randint(0, COUNT_THINGS_ON_PERS)
        choised_things = random.sample(things, limit)
        fighter.set_things(choised_things)
        if fighter.things:
            print(f'\n Боец "{fighter.name}" получил предметы:')
            for thing in fighter.things:
                print(colored(f'"{thing.name}"', 'green'))
        else:
            print(colored(
                f'\n Бойцу "{fighter.name}" не повезло, ему не выпало ничего!',
                'red'))


def burn_child(fighter_1, fighter_2):
    name = (fighter_1.name + fighter_2.name)[:10]
    defense = (fighter_1.defense + fighter_2.defense) / 2
    attack = (fighter_1.attack + fighter_2.attack) / 2
    health = (fighter_1.health + fighter_2.health) / 2
    sex = fighter_1.sex
    child = Child(name, defense, attack, health, sex)
    FIGHTERS.append(child)
    return child


def battle(fighter_1, fighter_2):
    freeze_health_1 = fighter_1.health
    freeze_health_2 = fighter_2.health
    attack_damage_1 = fighter_1.attack
    attack_damage_2 = fighter_2.attack
    if fighter_1.sex != fighter_2.sex and random.randint(0, 3) == 1:
        return burn_child(fighter_1, fighter_2)

    while True:
        fighter_2.decrease_helth(attack_damage_1)
        if fighter_2.health <= 0:
            if SURVIVAL:
                fighter_1.health = freeze_health_1
            return fighter_1
        fighter_1.decrease_helth(attack_damage_2)
        if fighter_1.health <= 0:
            if SURVIVAL:
                fighter_2.health = freeze_health_2
            return fighter_2


def main():
    count_battle = 0
    user_input()
    get_things(FIGHTERS, THINGS)
    print(colored('\n---------  FIGHT!  --------\n', 'yellow'))

    while True:
        len_fighters = len(FIGHTERS) - 2
        if len_fighters == -1:
            break
        limit = len(FIGHTERS) - 1
        fighter_1 = FIGHTERS.pop(random.randint(0, limit))
        fighter_2 = FIGHTERS.pop(random.randint(0, limit - 1))
        count_battle += 1
        print(colored(f'Бой №{count_battle} начался! '
              f'Участники: {fighter_1.name} и {fighter_2.name}.\n', 'magenta'))
        winner = battle(fighter_1, fighter_2)
        if len_fighters < len(FIGHTERS):
            print(f'В этом бою родился {winner.name}!\n')
            FIGHTERS.append(fighter_1)
            FIGHTERS.append(fighter_2)
        else:
            print(f'В этом бою победил {winner.name}!!!\n')
            FIGHTERS.append(winner)
    print(colored(
        f'    Поздравляем победителя {FIGHTERS[0].name}!!!', 'yellow'))


if __name__ == '__main__':
    main()
