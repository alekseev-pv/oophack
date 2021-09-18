from config import MAX_HP

class Thing:

    def __init__(self, title, damage, protection, health_point):
        self.title = title
        self.damage = damage
        self.protection = protection
        self.health_point = health_point


all_things = [
    Thing(
        title = 'Брильянтова сова',
        damage = 0.3 * MAX_HP,
        protection = 0,
        health_point = 0
    ),
    Thing(
        title = 'Большая хрустальная сова',
        damage = 0.1 * MAX_HP,
        protection = 0,
        health_point = 0
    ),
    Thing(
        title = 'Большая советская энциклопедия',
        damage = 0,
        protection = 0.1,
        health_point = 0
    ),
    Thing(
        title = 'Брошюрка',
        damage = 0,
        protection = 0.025,
        health_point = 0
    ),
    Thing(
        title = 'Хрустальный атом',
        damage = 0,
        protection = 0,
        health_point = 0.5 * MAX_HP
    ),
    Thing(
        title = 'Орден магистра',
        damage = 0.25 * MAX_HP,
        protection = 0.1,
        health_point = - 0.2 * MAX_HP
    ),
]