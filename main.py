from random import choice, randint, sample, shuffle

from build import Thing
from settings import NAMES_HEROES, NAMES_THINGS, PERSON_CLASSES


def make_things():
    things = []
    for name in NAMES_THINGS:
        things.append(Thing(
            name,
            randint(0, 10),
            randint(0, 10),
            randint(0, 3),
        ))
    return sorted(things, key=lambda x: x.protection)


def make_persons(count):
    persons = []
    names = sample(NAMES_HEROES, count)

    def make_random_person(person_name, immunity, power, life,):
        person_class = choice(PERSON_CLASSES)
        persons.append(person_class(person_name, immunity, power, life,))

    for name in names:
        make_random_person(
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


if __name__ == "__main__":
    all_heroes = dress_persons(
        make_persons(10),
        make_things(),
    )

    while len(all_heroes) > 1:
        make_arena(all_heroes)

    print(f'Победитель: {all_heroes}')
