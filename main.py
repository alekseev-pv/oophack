from typing import Dict, List, Optional, Tuple


class Thing:
    """
    Класс Thing описывает игровые вещи
    """

    def __init__(self, name,
                 defence, attack, life) -> None:
        """
        Принимает на вход:
        name - имя вещи,
        defence - защита,
        attack - нападение,
        life - жизнь.
        """
        self.name = name
        self.defence = defence
        self.attack = attack
        self.life = life


class Person:
    """
    Класс Person описывает основные параметры персонажа игры
    """
    pass


class Paladin:
    """
    Класс Paladin увеличивает оборонительные способности Персонажа
    """
    pass


class Warrior:
    """
    Класс Warrior увеличивает наступательные способности Персонажа
    """
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
