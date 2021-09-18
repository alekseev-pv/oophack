import random
from classes import Paladin, Warrior, ChuckNorris
from things import things

# Колличесво участнков битвы
n = 10
# Список возможных классов
list_of_person_classes = [Paladin, Warrior, ChuckNorris]
# Для создания списка из 20 имен использован генератор английских имен и
# фамилий с сайта randomus.ru
# Словарь имен персонажей (возможных участиков) и их характеристикв порядке
# hit_points, basic_attack, basic_protection. Поле со значением None
# задается рандомно. Без учета особенностей класса корактеристики следующие
# hit_points от 100 до 150 очков здоровья
# basic_attack от 20 до 35
# basic_protection от 0% до 0.29%
names_of_persons = {'Ryan Lee': [None, None, None],
                    'Lucille Green': [None, None, None],
                    'Brian Bennett': [None, None, None],
                    'Anne Anderson': [None, None, None],
                    'Roger Smith': [None, None, None],
                    'Kristen Wilson': [None, None, None],
                    'Debra McCoy': [None, None, None],
                    'Vicki Clark': [None, None, None],
                    'Michael Andrews': [None, None, None],
                    'James Rodriguez': [None, None, None],
                    'Jennifer Ball': [None, None, None],
                    'Jaime Rodriguez': [None, None, None],
                    'Pauline McDonald': [None, None, None],
                    'Anthony Reese': [None, None, None],
                    'Michael Harrison': [None, None, None],
                    'Brian Gibson': [None, None, None],
                    'Cheryl Hammond': [None, None, None],
                    'Naomi Curtis': [None, None, None],
                    'Jose Lee': [None, None, None],
                    'Curtis Tran': [None, None, None]}
# Список участников битвы
the_participants = []
# Создаем произвольно n персонажей
for i in range(n):
    name = random.choice(list(names_of_persons.keys()))
    if names_of_persons[name][0] is None:
        hit_points = random.randrange(100, 150, 10)
    else:
        hit_points = names_of_persons[name][0]
    if names_of_persons[name][1] is None:
        basic_attack = random.randint(20, 35)
    else:
        basic_attack = names_of_persons[name][1]
    if names_of_persons[name][2] is None:
        basic_protection = random.randint(0, 29) / 100
    else:
        basic_protection = names_of_persons[name][2]
    del names_of_persons[name]
    # Выбираем класс персонажа
    persons_class = random.choice(list_of_person_classes)
    # Создаем персонажа
    gladiator = persons_class(name,
                              hit_points,
                              basic_attack,
                              basic_protection)
    print(f'К участникам битвы присоединился {gladiator}.')
    print(f'У него {gladiator.hit_points} очков здороввья.')
    print(f'Сила его атаки - {gladiator.basic_attack}.')
    print(f'Коэффициент его защиты {gladiator.basic_protection}.')
    print()
    # Добавляем его к списку участников
    the_participants.append(gladiator)
# Одеваем персонажей рандомными вещами
for person in the_participants:
    # Задаем рандомное колличество вещей персонажа от 0 до 4
    number_of_things = random.randint(0, 4)
    # Выбираем несколько разных вещей
    random_things = random.choices(things, k=number_of_things)
    person.set_things(random_things)
