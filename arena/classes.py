import random


class Thing():

    def __init__(self,
                 item_name,
                 protection=None,
                 attack=None,
                 life=None):
        self.item_name = item_name
        # процент защиты не должен превышать 10%(0.1)
        if protection is None:
            self.protection = random.randint(0, 10) / 100
        else:
            self.protection = protection
        if attack is None:
            self.attack = random.randint(0, 10)
        else:
            self.attack = attack
        if life is None:
            self.life = random.randrange(0, 100, 10)
        else:
            self.life = life

    def __str__(self):
        return self.item_name


class Person():

    def __init__(self, name, hit_points, basic_attack, basic_protection):
        self.name = name
        # Базовые характеристики персонажа
        self.hit_points = hit_points
        self.basic_attack = basic_attack
        self.basic_protection = basic_protection
        # Уровень персонажа. Может быть использован для расчета
        # окончательных характеристик
        self.level = 1
        # Окончательные характеристики персонажа
        self.final_hit_points = hit_points * self.level
        self.final_attack = basic_attack * self.level
        self.final_protection = basic_protection * self.level
        # список вещей персонажа
        self.things = []

    def __str__(self):
        return self.name

    def set_things(self, things):
        """Метод, принимающий на вход список вещей"""
        self.things = things
        # Определяем колличество вещей персонажа
        number_of_things = len(self.things)
        # Если колличество вещей персонажа не 0
        if number_of_things:
            # Посчитаем суммарную прибавку характеристик
            life, attack, protection = 0, 0, 0
            for thing in self.things:
                life += thing.life
                attack += thing.attack
                protection += thing.protection
            # Окончательные характеристики персонажа
            self.final_hit_points += life
            self.final_attack += attack
            self.final_protection += protection
            list_things = list(map(str, self.things))
            print(f'{self.name} выбирает {", ".join(list_things)} и получает')
            print(f'прибавку по НР: {life}, по урону: {attack}, по защите:'
                  f'{protection:.2f}')
            print()
        else:
            print(f'{self.name} слишком уверен в себе и ничего не выбирает')
            print()

    def set_level(self, level):
        # Повышаем характеристики персонажа в соответствии с полученным
        # уровнем
        self.final_hit_points = self.hit_points * self.level
        self.final_attack = self.basic_attack * self.level
        self.final_protection = self.basic_protection * self.level
        # Восстанавливаем усилинеия от вещей
        self.set_things(self.things)

    def take_away(self, attacking):
        """Метод вычитания жизни на основе входной атаки"""
        attack = attacking.final_attack * (1 - self.final_protection)
        self.final_hit_points -= attack
        print(f'{attacking} наносит удар по {self.name} на {attack:.2f}'
              ' урона')
        print(f'и у него остается {self.final_hit_points:.2f} очков здоровья')
        print()


class Paladin(Person):
    """Количество присвоенных жизней и процент защиты умножается на 2"""
    def __init__(self, name, hit_points, basic_attack, basic_protection):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(name, hit_points, basic_attack, basic_protection)
        self.hit_points = hit_points * 2
        self.basic_protection = basic_protection * 2


class Warrior(Person):
    """Класс наследуется от персонажа, при этом атака умножается на 2"""
    def __init__(self, name, hit_points, basic_attack, basic_protection):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(name, hit_points, basic_attack, basic_protection)
        self.basic_attack = basic_attack * 2


class ChuckNorris(Person):
    """История умалчивает детали появления целой рассы Чаков Норрисов.

    Точно известно лишь то, что победить представителя этой рассы
    может только представитель этой рассы
    """
    def __init__(self, name, hit_points, basic_attack, basic_protection):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(name, hit_points, basic_attack, basic_protection)
        self.hit_points = basic_attack * 100500
        self.basic_attack = basic_attack * 100500
        self.basic_protection = basic_attack * 100500
