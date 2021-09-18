# предварительный список вещей с признаками (name, is_weapon, is_clothes,
# variants)
THINGS_PRE_LIST = (
    # оружие
    ('Световой меч', True, False,
     (' ситов', ' с боковыми лезвиями', ' c искревленной рукоятью',
      ' имперских рыцарей', '')),
    ('Граната', True, False,
     (' газовая', ' осколочная', ' светозвуковая', '')),
    ('Вибромеч', True, False,
     (' гаморреанский', '')),
    ('Бластер', True, False,
     (' легкий', ' автоматический', ' охотничий', '')),
    ('Огнемет', True, False,
     (' дальнобойный', '')),
    ('Дроид', True, False,
     ('-наемник', '-охранник', '-убийца', '')),
    # доспехи
    ('Броня', False, True,
     (' мандолорцев', ' сенатских коммандос', '')),
    ('Кимоно', False, True,
     (' джедая', ' сита')),
    ('Шлем', False, True,
     (' воина', ' охранника')),
    ('Сапоги', False, True,
     (' юнлинга', '')),
    ('Пояс', False, True,
     (' с гранатами', ' наемника', ' энергетический', '')),
    ('Щит', False, True,
     (' энергетический', ' отражающий', ' джедая', '')),
)

# список имен персонажей (name, is_unique)
PERSONS_PRE_LIST = (
    ('Дарт Вейдер', True),
    ('Сенатор Палптаин', True),
    ('Реван', True),
    ('Оби-Ван Кеноби', True),
    ('Квай-Гон Джинн', True),
    ('Магистр Йода', True),
    ('Люк Сайуокер', True),
    ('Лея Органа', False),
    ('Хан Соло', False),
    ('Боба Фетт', False),
    ('Джанго Фетт', False),
    ('Чубакка', False),
    ('R2-D2', False),
    ('Генерал Гривус', False),
    ('Лэндо Калриссиан', False),
    ('Ведж Антиллес', False),
    ('Джа-Джа Бинкс', False),
    ('Нут Ганрей', False),
    ('Адмирал Акбар', False),
    ('Уилхуфф Таркин', False),
)

# скилы уникальных персонажей
# name, is_attack, is_defence, attack_points_multiplicator,
# health_points_multiplicator, defence_points_multiplicator,
# uniq_skill, attack_repelling
PERSONS_SKILLS = (
    {
        'name': 'отбросил врага с помощью силы',
        'is_attack': True,
        'uniq_skill': True,
        'action': {'attack_points_multiplicator': 1.03}
    },
    {
        'name': 'залечил рану',
        'is_defence': True,
        'uniq_skill': True,
        'action': {'health_points_multiplicator': 1.05}
    },
    {
        'name': 'отразил удар врага',
        'is_defence': True,
        'uniq_skill': False,
        'action': {'attack_repelling': True}
    }
)

# настройки игры
# key: (min, max)
THING_SETTINGS = {
    'DefencePercent': (0, 10),
    'AttackPoints': (5, 15),
    'HealthPoints': (30, 50),
}
PERSON_SETTINGS = {
    'DefencePercent': (15, 30),
    'AttackPoints': (20, 30),
    'HealthPoints': (220, 300),
}
