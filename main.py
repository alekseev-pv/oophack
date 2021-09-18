import random

import names


class Thing:
    """
    Класс Thing описывает игровые вещи
    """

    def __init__(self, name,
                 defence_per, attack_per, hp_per) -> None:
        """
        Принимает на вход:
        name - имя вещи,
        defence_per - процент защиты,
        attack_per - процент нападения,
        hp_per - жизнь.
        """
        self.name = name
        self.defence_per = defence_per
        self.attack_per = attack_per
        self.hp_per = hp_per


class Person:
    """
    Класс Person описывает основные параметры персонажа игры
    """

    def __init__(self, name,
                 hp, base_attack, base_defence) -> None:
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.finalProtection = 0
        self.things = []

    def set_things(self, things):
        self.things = things
        self.finalProtection = self.get_final_protection()
        pass

    def get_final_protection(self):
        return self.base_defence + self.get_things_protection()

    def get_things_protection(self):
        return sum([x.defence_per for x in self.things])

    def got_attacked(self, attack_damage):
        self.hp = (self.hp - (attack_damage -
                   attack_damage*self.finalProtection))

    def attack(self):
        selected_thing = self.things[random.randint(
            0, len(self.things) - 1)]
        return selected_thing.attack_per

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True


class Paladin(Person):
    """
    Класс Paladin увеличивает оборонительные способности Персонажа
    """

    def __init__(self, name, hp, base_attack, base_defence) -> None:
        super().__init__(name, hp, base_attack, base_defence)
        self.hp = self.hp*2
        self.base_defence = self.base_defence * 2

    def __str__(self) -> str:
        return self.name


class Warrior(Person):
    """
    Класс Warrior увеличивает наступательные способности Персонажа
    """

    def __init__(self, name, hp, base_attack, base_defence) -> None:
        super().__init__(name, hp, base_attack, base_defence)
        self.base_attack = self.base_attack * 2

    def __str__(self) -> str:
        return self.name


def create_all_things():
    things = []
    for i in range(20):
        name = f'{names.get_last_name()}_thing'
        defence = random.uniform(0, 0.1)
        attack = random.uniform(0.01, 0.1)
        hp = random.uniform(0, 0.1)
        things.append(Thing(name, defence, attack, hp))
    things.sort(key=lambda x: x.defence_per)
    return things


def get_random_things(all_things):
    return [all_things[i] for i in range(random.randint(1, 4))]


def battle(first_warrior, second_warrior):
    while True:
        print(first_warrior.hp)
        print(second_warrior.hp)
        warrior_damage = round(first_warrior.attack(), 2)
        print(
            f'{first_warrior.name} наносит удар по '
            f'{second_warrior.name} на {warrior_damage} урона')
        second_warrior.got_attacked(warrior_damage)
        if not second_warrior.is_alive():
            print(f'{first_warrior.name} победил')
            return second_warrior
        warrior_damage = round(second_warrior.attack(), 2)
        print(
            f'{second_warrior.name} наносит удар по '
            f'{first_warrior.name} на {warrior_damage} урона')
        first_warrior.got_attacked(warrior_damage)
        if not first_warrior.is_alive():
            print(f'{second_warrior.name} победил')
            return first_warrior


def main() -> None:
    all_things = create_all_things()  # произвольноe количество вещей
    warrior_names = [f'{names.get_first_name()}_warrior'
                     for i in range(20)]  # список имен персонажей
    warrior_type = [Paladin, Warrior]  # тип война
    warriors = [warrior_type[random.randint(0, 1)](
        warrior_names[random.randint(
            0, len(warrior_names)-1)], 100, random.randint(5, 10),
        random.uniform(0.01, 0.1)) for i in range(0, 10)]  # список войнов
    for warrior in warriors:
        warrior.set_things(get_random_things(all_things))
    while len(warriors) != 1:
        first_warrior = warriors[random.randint(
            0, len(warriors)-1)]
        second_warrior = warriors[random.randint(
            0, len(warriors)-1)]
        while second_warrior == first_warrior:
            second_warrior = warriors[random.randint(
                0, len(warriors)-1)]
        lost_warrior = battle(first_warrior, second_warrior)
        warriors.remove(lost_warrior)
    print(f'{warriors[0].name} победил')


if __name__ == '__main__':
    main()
