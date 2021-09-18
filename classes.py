from typing import List


class Thing:
    """Класс вещи. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points)."""
    name: str
    defence_percent: int
    attack_points: float
    health_points: float

    def __init__(self, name, defence_percent, attack_points, health_points):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points


class Person:
    """Класс персонажа. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points)."""
    name: str
    defence_percent: int
    health_points: float
    attack_points: float
    things: List[Thing]

    def __init__(self, name, defence_percent, attack_points, health_points):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points

    def set_things(self, things):
        """Устанавливаем список вещей."""
        self.things = things

    def decrease_health_points(self, attack_damage):
        """Метод вычитания health_points экземпляра в зависимости от атаки
        attack_damage."""
        pass

    def __total_points(self, attrname):
        """Вычисление количества поинтов (атрибут передается в attrname)
        экземпляра."""
        points = getattr(self, attrname)
        try:
            points += sum([getattr(thing, attrname) for thing in self.things])
        except AttributeError:
            pass

        return points

    def total_defence_percent(self):
        """Вычисление количества поинтов защиты."""
        return self.__total_points('defence_percent')

    def total_attack_points(self):
        """Вычисление количества поинтов атаки."""
        return self.__total_points('attack_points')

    def total_health_points(self):
        """Вычисление количества поинтов здоровья."""
        return self.__total_points('health_points')


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
