import random

from models import persons_names, things_names


# Количество персонажей, одновременно участвующих в игре
PERS_NUMBER = 10
# Количество типов персонажей
PERS_CLASS_NUMBER = 2
# Максимальное количество вещей в одни руки
MAX_THING_NUMBER = 4


class Thing:
    """Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь; Это могут быть предметы одежды,
    магические кольца, всё что угодно)
    """
    def __init__(self, name, vitality, attack, defence) -> None:
        self.name = name
        self.vitality = vitality
        self.attack = attack
        self.defence = defence


class Person:
    """Универсальный персонаж - родительский класс"""

    MAX_DEFENCE = 0.1

    def __init__(self, name, vitality, attack, defence,) -> None:
        self.name = name
        self.vitality = vitality
        self.attack = attack
        if defence > self.MAX_DEFENCE:
            self.defence = self.MAX_DEFENCE
        else:
            self.defence = defence
        self.things = []

    def __str__(self):
        return self.name

    def set_things(self, things):
        to_set = []
        to_set.append(things)
        if len(to_set) + len(self.things) <= MAX_THING_NUMBER:
            self.things.append(to_set)
            for thing in to_set:
                self.vitality += thing.vitality
                self.attack += thing.attack
                self.defence += thing.defence
            return True
        else:
            print('I cant carry any more')
            return False

    def attack_damage(self, damage):
        final_damage = damage * (1 - self.defence)
        self.vitality -= final_damage


class Paladin(Person):
    """Класс наследуется от персонажа, при этом
    количество присвоенных жизней и процент защиты
    умножаются на 2 в конструкторе
    """
    def __init__(self, name, vitality, attack, defence) -> None:
        super().__init__(name, vitality, attack, defence)
        self.vitality = vitality * 2
        self.defence = defence * 2


class Warrior(Person):
    """Класс наследуется от персонажа, при этом атака
    умножается на 2 в конструкторе.
    """
    def __init__(self, name, vitality, attack, defence) -> None:
        super().__init__(name, vitality, attack, defence)
        self.attack = attack * 2


def create_things(number=random.randint(
        PERS_NUMBER, PERS_NUMBER*MAX_THING_NUMBER)):
    """Функция создания <number> количества
    вещей с различными параметрами
    """
    things = []
    thing_names_set = random.choices(things_names, k=number)
    for i in range(number):
        name = thing_names_set[i]
        vitality = random.randint(10, 100)
        attack = random.randint(1, 10)
        defence = random.randint(1, 10) / 100
        thing = Thing(name, vitality, attack, defence)
        things.append(thing)
    return sorted(things, key=lambda x: x.defence)


def class_pers_numbers(pers_number, class_number):
    """Функция случайным образом разбивает натуральное число
    на заданное количество целых неотрицательных слагаемых
    """
    if class_number >= pers_number:
        print('Число типов превысило или совпало с числом элементов')
        return pers_number
    p_number = []
    sum_number = 0  # текущая сумма элементов
    for i in range(class_number):
        p_number.append(random.randint(1, pers_number))
        sum_number += p_number[i]
    sum_number_f = 0
    for i in range(class_number - 1):
        p_number[i] = p_number[i] * pers_number // sum_number
        sum_number_f += p_number[i]
    p_number[-1] = pers_number - sum_number_f
    return p_number


def create_persons(number=PERS_NUMBER):
    """Функция создания <number> количества
    персонажей с различными параметрами
    """
    persons = []
    # Поскольку в данном варианте игры имена персонажей уникальны,
    # нужно застраховаться от превышения количеством создаваемых персонажей
    # количества имен в списке, если мы вдруг решим создать больше 10
    persons_names_max_number = len(persons_names)
    if number > persons_names_max_number:
        number = persons_names_max_number
    persons_names_set = random.sample(persons_names, number)

    # Определяем лимиты количества персонажей разных классов - случайно
    persons_class = 0
    class_limits = class_pers_numbers(number, PERS_CLASS_NUMBER)
    class_limit = class_limits[persons_class]
    # Создаем персонажей подряд по классам
    for i in range(number):
        name = persons_names_set[i]
        # Параметры желательно подобрать так,
        # чтобы <vitality> не являлся определяющим.
        vitality = random.randint(2000, 3000)
        attack = random.randint(30, 50)
        defence = random.randint(1, 10) / 100
        # Определяем класс персонажа в рамках лимита
        if persons_class == 0:
            person = Paladin(name, vitality, attack, defence)
        elif persons_class == 1:
            person = Warrior(name, vitality, attack, defence)
        # по идее, исключений быть не должно, но на всякий случай
        else:
            person = Person(name, vitality, attack, defence)
        # Переключаемся на следующий класс при достижении лимита
        persons.append(person)
        if i == class_limit:
            persons_class += 1
            class_limit += class_limits[persons_class]
    return persons


def persons_items_distrib(persons, things):
    """Функция распределения вещей по персонажам"""

    # создаем минимум для распределения каждому персонажу
    min_stack = []
    min_stack_len = len(persons)
    distrib_list = things
    if len(distrib_list) >= min_stack_len:
        for i in range(min_stack_len):
            thing_num = random.randint(0, len(distrib_list)-1)
            min_stack.append(things[thing_num])
            distrib_list.remove(things[thing_num])

    # выдаем каждому по-минимуму
    for person in persons:
        person.set_things(min_stack[0])
        min_stack.remove(min_stack[0])

    # раздаем оставшиеся вещи случайно с учетом лимитов
    pers_list = persons
    for thing in distrib_list:
        person = random.choice(pers_list)
        pers_index = persons.index(person)
        persons[pers_index].set_things(thing)
        distrib_list.remove(thing)
        if len(persons[pers_index].things) == MAX_THING_NUMBER:
            pers_list.remove(person)


def match(persons):
    """Алгоритм проведения турнира-арены между персонажами"""

    pers_list = persons
    while len(pers_list) > 1:
        rivals_nums = random.sample(range(len(pers_list)), 2)
        # 0 - защищающийся, 1 - нападающий
        damage = pers_list[rivals_nums[1]].attack
        pers_list[rivals_nums[0]].attack_damage(damage)
        print(f'{pers_list[rivals_nums[1]]} нанёс урон позиции '
              f'{pers_list[rivals_nums[0]]} на {damage} единиц')
        if pers_list[rivals_nums[0]].vitality <= 0:
            print(f'{pers_list[rivals_nums[0]]} покидает арену')
            del pers_list[rivals_nums[0]]

    print(f'Победителем турнира объявляется {pers_list[0]}')


def runner():
    things = create_things()
    persons = create_persons()
    persons_items_distrib(persons, things)
    match(persons)


runner()
