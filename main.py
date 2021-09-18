from random import choice, randrange

from characters import Paladin, Warrior
from things import Thing

character_names = (
    'Люций Вечный', 'Фулгрим Фениксиец', 'Лукас Трикстер',
    'Леман Русс', 'неизвестный гвардеец', 'Аркхам Ленд', 'Слаанешь',
    'Феленид', 'Хорус Луперкаль', 'Геноведьма', 'Нургл',
    'Тиран Улья', 'Омниссия', 'Ангрон раб Нуцерии', 'Сангвиний',
    'Мортарион', 'Тифус', 'Космодесантник', 'Техножрец', 'Альфа псайкер',
    'Малкадор Сигилит', 'Тзинч', 'Магнус Красный', 'Константин Вальдор')

weapon_names = (
    'Демонический клинок', 'Болтер', 'Пилотопор', 'Лазган',
    'Ножка от стола', 'Бочонок с Мъёдом', 'Варп Даст',
    'Благословение Императора', 'Цепной меч', 'Пустотный щит',
    'Черная ярость', 'Огнемёт', 'Стаббер', 'Заточка',
    'Оторванная рука сервитора', 'Силовая Броня', 'Силовой клинок', 'Археотех')


def generate_person(names):
    persons = {}
    x = 0
    counter = randrange(8)
    while x < counter:
        name_person = choice(names)
        persons[x] = Paladin(name_person, randrange(
            20, 80), randrange(5, 75), randrange(25, 200))
        x += 1
    while x < 10:
        name_person = choice(names)
        persons[x] = Warrior(name_person, randrange(
            10, 60), randrange(10, 110), randrange(50, 300))
        x += 1
    return persons


def generate_weapon(names):
    weapon_list = {}
    x = 0
    for item in names:
        weapon_list[x] = Thing(item, randrange(
            0, 20), randrange(0, 10), randrange(0, 75))
        x += 1
    return weapon_list


def generate_thing(weapons):
    items = []
    x = 0
    while x <= randrange(3):
        item_id = randrange(0, len(weapons))
        items.append(weapons[item_id])
        x += 1
    return items


def equip_characters(persons, weapons):
    x = 0
    while x < len(persons):
        items = generate_thing(weapons)
        persons[x].set_things(items)
        x += 1


def player_vs_player(person_one, person_two):
    person_one_hp = person_one.base_hp
    person_one_attack = person_one.base_attack
    person_one_deff = person_one.base_deff
    person_two_hp = person_two.base_hp
    person_two_attack = person_two.base_attack
    person_two_deff = person_two.base_deff
    while (person_one_hp >= 0) or (person_two_hp >= 0):
        damage = person_two_attack - \
            (person_two_attack * round(person_one_deff/1000))
        print(f'{person_two.name} наносит удар по {person_one.name}'
              f' на {damage} урона.')
        person_one_hp -= damage
        print(f' У {person_one.name} осталось {person_one_hp} хп.')
        if person_one_hp <= 0:
            print(f'{person_one} погиб. Победитель этого раунда {person_two}!')
            return person_two

        damage = person_one_attack - \
            (person_one_attack * round(person_two_deff/1000))
        print(f'{person_one.name} наносит удар по {person_two.name}'
              f' на {damage} урона.')
        person_two_hp -= damage
        print(f' У {person_two.name} осталось {person_two_hp} хп.')
        if person_two_hp <= 0:
            print(f'{person_two} погиб. Победитель этого раунда {person_one}!')
            return person_one


def epic_battle(persons):
    alive_persons = list(persons.values())
    while len(alive_persons) > 1:
        person_one_id = randrange(0, len(alive_persons))
        person_one = alive_persons[person_one_id]
        alive_persons.remove(person_one)
        person_two_id = randrange(0, len(alive_persons))
        person_two = alive_persons[person_two_id]
        alive_persons.remove(person_two)
        print(f'Бой между {person_one.name} и {person_two.name}')
        winner = player_vs_player(person_one, person_two)
        alive_persons.append(winner)
    print(f'Чемпион турнира: {alive_persons[0].name.upper()}!!!')
    print(
        f'{alive_persons[0].name} выигрывает квартиру в мире Улье'
        f'и один купон на бесплатный Exterminatus!')
    print(f'С вами была передача: "Обычный день в Вархаммере", '
          f'новый выпуск - каждые 10000 лет!')
