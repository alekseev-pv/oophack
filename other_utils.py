from random import randint, uniform, shuffle, choice

from person import Person
from specialization import Paladin, Warrior
from things import Thing

beautify_wear = []  # красивое название, когда надевается вещь

fill_things = ['Меч Артура', 'Распределяющая шляпа', 'Куртка Фрая', 'Очки Поттера',
               'Зубочистка', 'Щит Кэпа', 'Молот Тора', 'Плащ последней надежды', 'Ожерелье Сатаны',
               'Мышка с острыми краями', 'Кроличья лапка', 'Бузиная палочка', 'Очки шизофрении',
               'Кувалда Разврата', 'Штаны мускулинности с кармашком для яиц', 'Плащ презрения',
               'Перчатки Ябеды-корябеды', 'Свинский Посох победы', 'Маринованные Латы', 'Кольчуга безрассудства',
               'Кольцо Всепьянствия', 'Огненное Ожерелье Оракула', 'Стальные стринги', 'Омерзительная Рубашка']

names_for_percs = ['Гендальф', 'Артас', 'Гаррош', 'Генерал-адмирал Алладин', 'Борис Сергеевич',
                   'Страж морепродуктов', 'Кыса-ногоцап', 'Веган-потрошитель',
                   'Кровавый Володя', 'Саблезубый Пикачу', 'Птичья личность', 'Авокадыш', 'Свин-картежник']

map_spec_icons = {
    'Paladin': 'o',
    'Warrior': 'w',
    'Person': 'x'
}


def create_stuff(count=len(fill_things), need_print=False):
    def sort_key(s):
        return s.defense

    list_items = []
    if count > len(fill_things):
        count = len(fill_things)
    for i in range(count):
        shuffle(fill_things)
        elem = fill_things.pop()
        attack = randint(0, 200)
        defense = round(uniform(0, .15), 2)
        hp = randint(0, 200)
        thing = Thing(name=elem, attack=attack, defense=defense, hp=hp)
        if need_print:
            print(f'Создан предмет - {thing}!')
        list_items.append(thing)
    result = sorted(list_items, key=sort_key)
    # print(f'Создано {count} предметов')
    return result


def create_percs(count=len(names_for_percs), need_print=False):
    def fill_percs(name_specialization=Person, num_objects=0, points=None):
        if points is None:
            points = []
        for i in range(num_objects):
            shuffle(names_for_percs)
            name = names_for_percs.pop()
            attack = randint(10, 200)
            defense = round(uniform(0, .05), 2)
            hp = randint(100, 1000)
            speed = randint(19, 21)
            point = [randint(0, 100), randint(0, 100)]
            while point in points:
                point = [randint(0, 100)]
            points.append(point)
            perc = name_specialization(name=name, attack=attack, defense=defense, hp=hp,
                                       speed=speed, point=point)
            list_percs.append(perc)
        # print(f'Создано {num_objects} персонажей класса {name_specialization.spec_name}\n')

    positions = []
    list_percs = []
    if count > len(names_for_percs):
        count = len(names_for_percs)
    num_pal = randint(1, count - 1)
    num_war = count - num_pal

    fill_percs(name_specialization=Paladin, num_objects=num_pal, points=positions)
    fill_percs(name_specialization=Warrior, num_objects=num_war, points=positions)

    return list_percs


def equip_percs(percs, items, slow_time = 0):
    wear_list = []
    for perc in percs:
        n_items = randint(1, 4)
        perc_wear = []
        for i in range(n_items):
            if items:
                shuffle(items)
                item = items.pop()
                wear_list.append(item)
                perc_wear.append(item)
            perc.set_things(perc_wear)
    # print('Персонажы экипированы и готовы к бою!\n')
