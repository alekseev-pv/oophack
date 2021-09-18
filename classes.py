from typing import List


class Thing:
    """Класс вещи. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points),
    - признак оружия (is_weapon),
    - признак одежды (is_clothes)."""
    name: str
    defence_percent: int
    attack_points: float
    health_points: float
    is_weapon: bool
    is_clothes: bool

    def __init__(self, name, defence_percent, attack_points, health_points,
                 is_weapon, is_clothes):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points
        self.is_weapon = is_weapon
        self.is_clothes = is_clothes


class Person:
    """Класс персонажа. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points)."""
    name: str
    defence_percent: int
    final_protection: float
    health_points: float
    attack_points: float
    things: List[Thing]

    def __init__(self, name, defence_percent, attack_points, health_points):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points

        self.__recalculate_final_protection()

    def __total_points(self, attrname):
        """Вычисление количества поинтов (атрибут передается в attrname)
        экземпляра."""
        points = getattr(self, attrname)
        try:
            points += sum([getattr(thing, attrname) for thing in self.things])
        except AttributeError:
            pass

        return points

    def __recalculate_final_protection(self):
        self.final_protection = self.total_defence_percent() / 100

    def set_things(self, things):
        """Устанавливаем список вещей."""
        self.things = things
        self.__recalculate_final_protection()

    def decrease_health_points(self, attack_damage):
        """Метод вычитания health_points экземпляра в зависимости от атаки
        attack_damage."""
        health_points = self.health_points - attack_damage * (
                    1 - self.final_protection)

        self.health_points = 0 if health_points < 0 else health_points

    def total_defence_percent(self):
        """Вычисление количества поинтов защиты."""
        return self.__total_points('defence_percent')

    def total_attack_points(self):
        """Вычисление количества поинтов атаки."""
        return self.__total_points('attack_points')

    def total_health_points(self):
        """Вычисление количества поинтов здоровья."""
        return self.__total_points('health_points')

    def total_final_protection(self):
        return self.final_protection


class Paladin(Person):
    """Класс Паладина. Наследуется от Person."""

    def __init__(self, name, defence_percent, attack_points, health_points):
        super().__init__(name, defence_percent, attack_points, health_points)

        self.health_points *= 2
        self.defence_percent *= 2


class Warrior(Person):
    """Класс Воина. Наследуется от Person."""

    def __init__(self, name, defence_percent, attack_points, health_points):
        super().__init__(name, defence_percent, attack_points, health_points)

        self.attack_points *= 2


class Game:
    """Класс процесса игры."""

    def create_things(self):
        pass
