import random


class Heroes():

    def __init__(self, limit):
        self.limit = limit
        self.pattern = {'name': None,
                        'health_points': None,
                        'attack_points': None,
                        'defence_points': None}

        self.heroes = ['Арнольд Шварценеггер',
                       'Джеки Чан',
                       'Сильвестр Сталлоне',
                       'Чак Норрис',
                       'Дольф Лундгрен',
                       'Жан-Клод Ван Дамм',
                       'Брюс Уиллис',
                       'Уэсли Снайпс',
                       'Боло Йенг',
                       'Рутгер Хауэр',
                       'Лоренцо Ламас',
                       'Майкл Дудикофф',
                       'Синтия Ротрок',
                       'Джет Ли',
                       'Мел Гибсон',
                       'Брюс Ли',
                       'Дэнни Трехо'
                       'Стивен Сигал',
                       'Курт Рассел',
                       'Микки Рурк',
                       'Мистер Ти']

        self.skills = {'health_points': (150, 200),
                       'attack_points': (15, 20),
                       'defence_points': (10, 15)
                       }

    def make_a_pattern(self):

        i = random.randint(0, self.limit)
        self.pattern = {'name': self.heroes.pop(i),
                        'health_points':
                        random.randint(self.skills['health_points'][0],
                                       self.skills['health_points'][1]),
                        'attack_points':
                        random.randint(self.skills['attack_points'][0],
                                       self.skills['attack_points'][1]),
                        'defence_points':
                        random.randint(self.skills['defence_points'][0],
                                       self.skills['defence_points'][1])}

        self.limit -= 1
        return(self.pattern)

    def __str__(self):
        return(f"{self.pattern['name']}, {self.pattern['health_points']}, "
               f"{self.pattern['attack_points']}, {self.pattern['defence_points']}")
