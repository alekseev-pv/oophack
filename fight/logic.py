from random import choice, randint, sample, shuffle

import fight.settings as sett
from fight.build import Thing


def make_things():
    things = []
    for name in sett.NAMES_THINGS:
        things.append(Thing(
            name,
            randint(0, 10),
            randint(0, 10),
            randint(0, 3),
        ))
    return sorted(things, key=lambda x: x.protection)


def make_persons(count):
    persons = []
    names = sample(sett.NAMES_HEROES, count)

    def make_random_person(*args):
        person_class = choice(sett.PERSON_CLASSES)
        persons.append(person_class(*args))

    for i, name in enumerate(names):
        make_random_person(
            i + 1,
            name,
            randint(0, 10),
            randint(0, 10),
            randint(1, 3),
        )
    return persons


def dress_persons(persons, things):
    for person in persons:
        added_things = sample(things, randint(1, 4))
        person.set_things(added_things)
    return persons


def battle(attacker, defender):
    if defender.life > 0:
        damage = attacker.final_power - \
                 attacker.final_power * \
                 (defender.final_protection / 100)
        damage = round(damage, 2)
        print(f'{attacker} наносит удар по {defender} на {damage}')
        defender.get_hit(damage)
    return defender.life


def make_arena(heroes):
    shuffle(heroes)
    for attacker in heroes:
        for defender in heroes:
            if attacker != defender:
                if battle(attacker, defender) <= 0:
                    heroes.remove(defender)
                    print(f'выбыл {defender}')


def get_user_balance():
    if 'GLOBAL_USER_BALANCE' not in globals():
        global GLOBAL_USER_BALANCE
        GLOBAL_USER_BALANCE = sett.START_BALANCE
    return float(GLOBAL_USER_BALANCE)
