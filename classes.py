class Thing:
    """Класс вещи. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent). Указывается числом от 0 до 1,
    - количество атаки (attack_points),
    - количество жизней (health_points)."""
    name: str
    defence_points: float
    attack_points: float
    health_points: float

    def __init__(self, name, defence_points, attack_points, health_points):
        self.name = name
        self.defence_points = defence_points
        self.attack_points = attack_points
        self.health_points = health_points


class Person:
    name: str
    defence_points: float
    health_points: float
    attack_points: float

    def __init__(self, name, defence_points, attack_points, health_points):
        self.name = name
        self.defence_points = defence_points
        self.attack_points = attack_points
        self.health_points = health_points

    def set_things(self, things):
        pass

    def decrease_hp(self, foe_attack_points):
        pass


class Paladin(Person):
    def __init__(self, name, defence_points, attack_points, health_points):
        super().__init__(name, defence_points, attack_points, health_points)

        self.health_points *= 2
        self.defence_points *= 2


class Warrior(Person):
    def __init__(self, name, defence_points, attack_points, health_points):
        super().__init__(name, defence_points, attack_points, health_points)

        self.attack_points *= 2

