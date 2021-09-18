from things import Thing




all_player_names = [
    'Александр Друзь',
    'Максим Поташев',
    'Алесь Мухин',
    'Андрей Козлов',
    'Ровшан Аскеров',
    'Юлия Лазарева',
    'Федор Двинятин',
    'Михаил Скипский',
    'Илья Новиков',
    'Балаш Касумов',
    'Елена Орлова',
    'Елена Потанина',
]

class Person:

    def __init__(self, name, damage, protection, health_point):
        self.name = name
        self.damage = damage
        self.protection = protection
        self.health_point = health_point
        self.init_health_point = self.health_point
        self.things = []
        self.is_alive = True
        self.class_name = None
        self.damage_taken = 0
        self.damage_dealt = 0

    
    def set_things(self, things: list[Thing]):
        self.things.extend(things)
        for thing in things:
            self.damage += thing.damage
            self.protection += thing.protection
            self.health_point += thing.health_point
    
    def take_damage(self, damage):
        self.health_point -= damage
        self.damage_taken += damage

        if self.health_point <= 0:
            self.is_alive = False
    
    def attack(self, defender):
        attack_damage = self.damage * (1 - defender.protection)
        defender.take_damage(attack_damage)
        self.damage_dealt += attack_damage
        return attack_damage

class Paladin(Person):

    PALADIN_MULTIPLIER = 1.3

    def __init__(self, name, damage, protection, health_point):
        super().__init__(name, damage, protection, health_point)
        self.protection *= self.PALADIN_MULTIPLIER
        self.health_point *= self.PALADIN_MULTIPLIER
        self.init_health_point = self.health_point
        self.class_name = 'Паладин'


class Warrior(Person):

    WARRIOR_MULTIPLIER = 2

    def __init__(self, name, damage, protection, health_point):
        super().__init__(name, damage, protection, health_point)
        self.damage *= self.WARRIOR_MULTIPLIER
        self.class_name = 'Воин'


CHARACTER_CLASSES = [Paladin, Warrior]