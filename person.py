import math


class Person:
    spec_name = 'No class'

    def __init__(self, name, attack, defense, hp, speed, point):
        self.things = []
        self.name = name
        self.final_hp = hp
        self.final_protection = round(defense, 2)
        self.final_attack = round(attack)
        self.speed = speed
        self.point = point
        self.type_attack = 'melee'
        self.radius_attack = 3
        # print(f'Персонаж {self.name} создан!')

    def __str__(self):
        person_out = (f'{self.name} - {self.spec_name}\n'
                      f'точка на карте: {self.point}\n'
                      f'скорость: {self.speed}\n'
                      f'атака: {self.final_attack}\n'
                      f'защита: {self.final_protection}\n'
                      f'здоровье: {self.final_hp}' + '\n' + 20 * '- ')
        return person_out

    # def __repr__(self):
    #     return f'"{self.name}"'

    def set_things(self, things, is_log=False):
        self.things = things[:3]
        for thing in self.things:
            self.final_hp += thing.hp
            self.final_protection = round(self.final_protection + thing.defense, 2)
            self.final_attack += thing.attack
            if is_log:
                print(f'{self.name} с гордостью надевает: {thing.name}' + '\n' + 20 * '- ')
                # "с гордостью надевает" -> beautify_wear

    def drop_things(self):
        pass

    def under_attack(self, attacker, is_log=False):
        self.final_hp = round(self.final_hp - attacker.final_attack * (1 - self.final_protection))
        if self.final_hp <= 0:
            self.final_hp = 0
        if is_log:
            if self.final_hp == 0:
                print(f'{self.name} повержен!')
            else:
                # можно добавить другие фразы в зависимости от оставшегося хп, входящего и фактически нанесенного урона
                print(f'У {self.name} осталось {self.final_hp}')
        return {
            "attack_power": attacker.final_attack,
            "final_protection": self.final_protection,
            "hp_after_attack": self.final_hp}

    def get_person_items(self):
        return self.things

    def simple_distance(self, target):
        distance = math.sqrt(((self.point[0] - target.point[0]) ** 2) + ((self.point[1] - target.point[1]) ** 2))
        return round(distance, 2)

    def move_2d(self, target, space, move_distance):
        x = target.point[0] - self.point[0]
        y = target.point[1] - self.point[1]
        c = space
        if c == 0:
            c = 1
        cos_ = round(x / c, 2)
        sin_ = round(y / c, 2)
        a = move_distance * cos_
        b = move_distance * sin_
        return [a, b]

    def run_to_target(self, target):
        target_space = self.simple_distance(target) - self.radius_attack + 1
        if self.speed > abs(target_space):
            move = self.move_2d(target, target_space, target_space)
        else:
            move = self.move_2d(target, target_space, self.speed)

        self.point[0] = round(self.point[0] + move[0], 2)
        self.point[1] = round(self.point[1] + move[1], 2)
