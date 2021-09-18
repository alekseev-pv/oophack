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
    ('Сенатор Палпатин', True),
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
# name - текст скилла,
# is_attack - выполняется во время атаки,
# is_defence - выполняется во время защиты,
# unique_skill - скил только для уникальных персонажей,
# probability - вероятность выпадения скила
# типы скилов:
# attack_points_multiplicator - умножаем поинты атаки на это число (атака),
# health_points_multiplicator - умножаем поинты здоровья на это число (защита),
# attack_repelling - отражение атаки, здоровье не уменьшается (защита),
# contrattack - контратака, защищающийся бьет атакующего (защита)
PERSONS_SKILLS = (
    {
        'name': 'отбросил врага с помощью силы',
        'is_attack': True,
        'unique_skill': True,
        'actions': {'attack_points_multiplicator': 1.05},
        'probability': 0.05
    },
    {
        'name': 'подбросил гранату',
        'is_attack': True,
        'actions': {'attack_points_multiplicator': 1.1},
        'probability': 0.04
    },
    {
        'name': 'залечил рану',
        'is_defence': True,
        'unique_skill': True,
        'actions': {'health_points_multiplicator': 1.15},
        'probability': 0.1
    },
    {
        'name': 'отразил удар врага',
        'is_defence': True,
        'actions': {'attack_repelling': True},
        'probability': 0.07
    },
    {
        'name': 'ввел врага в заблуждение с помощью силы и тот промахнулся',
        'is_defence': True,
        'unique_skill': True,
        'actions': {'attack_repelling': True},
        'probability': 0.4
    },
    {
        'name': 'увернулся от атаки',
        'is_defence': True,
        'actions': {'attack_repelling': True, 'contrattack': True},
        'probability': 0.02
    }
)
