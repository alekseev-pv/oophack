import random
from time import sleep

from colorama import init
from models.things import Thing, sort_key
from models.warriors import Paladin, Warrior
from termcolor import colored

init()
print(colored('\n\n_____ START GAME  _____\n\n', 'yellow'))

COUNT_THINGS_ON_PERS = 4

THINGS = sorted([
    Thing('Socks of Fortune', random.randint(0, 20) / 100,
          random.randint(0, 100), random.randint(0, 100)),
    Thing('Gods armor', 0.1, 0, 100),
    Thing('killing rage', 0, 100, 0),
    Thing('Ring of Health', 0, 0, 100),
    Thing('Ring of Power', 0.02, 5, 0),
], key=sort_key)

FIGHTERS = [
    Warrior('Deathman', 0.1, 20, 5),
    Warrior('Halk', 0.2, 20, 20),
    Paladin('Grut', 0.2, 10, 30),
    Paladin('King of Night', 0.3, 10, 40)
]


SURVIVAL = False


def create_person(klasse):
    gamer = klasse(
        name=input('Введите имя: '),
        defense=float(input('Установите защиту от 0 до 0.5:  ')),
        attack=float(input('Установите атаку от 0 до 20:  ')),
        health=float(input('Установите злоровье от 0 до 50:  ')), )
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
        sleep(1)


def battle(fighter_1, fighter_2):
    freeze_health_1 = fighter_1.health
    freeze_health_2 = fighter_2.health
    attack_damage_1 = fighter_1.attack
    attack_damage_2 = fighter_2.attack
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
    sleep(2)
    print(colored('\n---------  FIGHT!  --------\n', 'yellow'))
    while True:
        if len(FIGHTERS) == 1:
            break
        limit = len(FIGHTERS) - 1
        fighter_1 = FIGHTERS.pop(random.randint(0, limit))
        fighter_2 = FIGHTERS.pop(random.randint(0, limit - 1))
        count_battle += 1
        print(colored(f'Бой №{count_battle} начался! '
              f'Участники: {fighter_1.name} и {fighter_2.name}.\n', 'magenta'))
        winner = battle(fighter_1, fighter_2)
        sleep(2)
        print(f'В этом бою победил {winner.name}!!!\n')
        FIGHTERS.append(winner)
    print(colored(
        f'    Поздравляем победителя {FIGHTERS[0].name}!!!', 'yellow'))


if __name__ == '__main__':
    main()
