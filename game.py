from random import choice, randint

"""Описываем константы, управляющие классом Thing."""
COUNT_THINGS = 40
THINGS_NAME = ['Кольцо', 'Мундир', 'Перчатки', 'Шлем', 'Штаны', 'Ботинки',
               'Ремень', 'Ожерелье']
THINGS_QUALITY = [' всевластия', ' доблести', ' забвения', ' могущества',
                  ' презрения', ' успеха', ' везения', ' удачи', ' разрушения']
MAX_THING_PROTECTION = 10
MIN_THING_PROTECTION = 1
MAX_THING_ATTACK = 20
MIN_THING_ATTACK = 5
MAX_THING_HP = 50
MIN_THING_HP = 20

"""Описываем константы, управляющие классом Person."""
COUNT_PERSON = 10
CLASS_PERSON = ['paladin', 'warrior']
PERSON_NAME = ['Орёл', 'Ястреб', 'Сокол', 'Коршун', 'Тигр', 'Волк',
               'Медведь', 'Гепард']
PERSON_QUALITY = [' храбрый', ' везучий', ' славный', ' могучий', ' грозный',
                  ' доблестный', ' забытый', ' счастливый', ' уничтожитель']
MAX_PERSON_PROTECTION = 20
MIN_PERSON_PROTECTION = 10
MAX_PERSON_ATTACK = 30
MIN_PERSON_ATTACK = 10
MAX_PERSON_HP = 100
MIN_PERSON_HP = 50
MAX_THINGS_ON_PERSON = 4
MIN_THINGS_ON_PERSON = 1


class Thing:
    """Создание класса Thing."""
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp

    def __str__(self):
        return self.name


class Person:
    """Создание класса Person."""
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection

    def set_things(self, things, count):
        """Метод одевания на объект класса необходимого количества (count)
           вещей из списка (things).
        """
        for i in range(count):
            thing = choice(things)
            things.remove(thing)
            self.hp += thing.hp
            self.base_attack += thing.attack
            self.base_protection += thing.protection
            print(f'надел "{thing}": здоровье - {thing.hp},'
                  f'атака - {thing.attack}, защита - {thing.protection}')

    def after_damage(self, attack_damage):
        """Метод преобразования входящего урона (attack_damage) в полученный
           (damage) через коэффициент (protection) защиты и расчёта
           оставшегося здоровья.
        """
        protection = self.base_protection / 100
        damage = int(attack_damage - attack_damage * protection)
        self.hp -= damage
        if self.hp > 0:
            return True, damage
        return False, damage

    def __str__(self):
        return self.name


class Paladin(Person):
    """Создание класса Paladin, дочернего от Person."""
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack, base_protection)
        self.hp = hp * 2
        self.base_protection = base_protection * 2
        self.class_name = 'Паладин'


class Warrior(Person):
    """Создание класса Warrior, дочернего от Person."""
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack, base_protection)
        self.base_attack = base_attack * 2
        self.class_name = 'Воин'


"""Создаём список случайных доспехов."""
things = []
for i in range(COUNT_THINGS):
    things.append(Thing(choice(THINGS_NAME) + choice(THINGS_QUALITY),
                        randint(MIN_THING_PROTECTION, MAX_THING_PROTECTION),
                        randint(MIN_THING_ATTACK, MAX_THING_ATTACK),
                        randint(MIN_THING_HP, MAX_THING_HP)))
    print(f'Создан доспех "{things[i]}": здоровье - {things[i].hp}, '
          f'атака - {things[i].attack}, защита - {things[i].protection}')
print()
"""Создаём список случайных персонажей."""
persons = []
for i in range(COUNT_PERSON):
    class_person = choice(CLASS_PERSON)
    if class_person == 'paladin':
        persons.append(Paladin(choice(PERSON_NAME) + choice(PERSON_QUALITY),
                               randint(MIN_PERSON_HP, MAX_PERSON_HP),
                               randint(MIN_PERSON_ATTACK, MAX_PERSON_ATTACK),
                               randint(MIN_PERSON_PROTECTION,
                                       MAX_PERSON_PROTECTION)))
    elif class_person == 'warrior':
        persons.append(Warrior(choice(PERSON_NAME) + choice(PERSON_QUALITY),
                               randint(MIN_PERSON_HP, MAX_PERSON_HP),
                               randint(MIN_PERSON_ATTACK, MAX_PERSON_ATTACK),
                               randint(MIN_PERSON_PROTECTION,
                                       MAX_PERSON_PROTECTION)))

    print(f'Создан "{persons[i].class_name}" по имени "{persons[i]}": '
          f'Здоровье - {persons[i].hp}, '
          f'Базовая атака - {persons[i].base_attack}, '
          f'Базовая защита - {persons[i].base_protection}')
print()
"""Одеваем персонажей в случайные вещи."""
for person in persons:
    print(f'{person.class_name} "{person}": Здоровье - {person.hp}, '
          f'Базовая атака - {person.base_attack}, '
          f'Базовая защита - {person.base_protection}')
    person.set_things(things, randint(MIN_THINGS_ON_PERSON,
                                      MAX_THINGS_ON_PERSON))
    print(f'и теперь обладает: Здоровье - {person.hp}, '
          f'Атака - {person.base_attack}, Защита - {person.base_protection}')
    print()
"""Битва. Принцип битвы: на каждом этапе выбирается два случайных персонажа,
   один - атакующий, второй - обороняющийся. Атакующий наносит урон, если
   защищающий выживает, то запускаем новый раунд, если погибает, то персонаж
   убирается из списка и запускается новый раунд среди оставшихся персонажей.
"""
print('Начинаем битву:')
while len(persons) > 1:
    attacker_index = randint(0, len(persons)-1)
    defender_index = randint(0, len(persons)-1)
    while defender_index == attacker_index:
        defender_index = randint(0, len(persons)-1)
    attacker = persons[attacker_index]
    defender = persons[defender_index]
    result = defender.after_damage(attacker.base_attack)
    print(f'{attacker.class_name} "{attacker}" наносит {attacker.base_attack} '
          f'урона по "{defender}" и отнимает {result[1]} жизни')
    if result[0]:
        print(f'{defender.class_name} "{defender}" стойко переносит удар, у '
              f'него осталось {defender.hp} здоровья')
    else:
        persons.remove(defender)
        print(f'{defender.class_name} "{defender}" погибает')
    print()
print(f'{persons[0].class_name} "{persons[0]}" побеждает, '
      f'у него осталось {persons[0].hp} здоровья')
