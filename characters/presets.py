THINGS_PRE_LIST = (
    ('Меч из стигийской стали', True, False,
     (' нико', ' аида', ' клития',
      ' имперских рыцарей', '')),
    ('Дракон', True, False,
     ('дымящий', ' огненный', ' светозвуковой', '')),
    ('Копье', True, False,
     (' вакандское', '')),
    ('Бластер', True, False,
     (' легкий', ' автоматический', ' охотничий', '')),
    ('Огнемет', True, False,
     (' краткоствольный', '')),
    ('джон уик', True, False,
     ('-наемник', '-охранник', '-убийца', '')),
    ('Броня из стигйской стали', False, True,
     (' аида', ' нико', '')),
    ('щит', False, True,
     (' уилла', ' нико')),
    ('Шлем', False, True,
     (' нико', ' уилла')),
    ('Сапоги', False, True,
     (' нико', '')),
    ('силовое поле', False, True,
     (' полное', ' частичное', '')),
)

PERSONS_PRE_LIST = (
    ('Нико ди анжело', True),
    ('Перси Джексон', True),
    ('Уилл Соллас', True),
    ('Аид', True),
    ('Апполон', True),
    ('Хирон', True),
    ('Бестия', True),
    ('Джуди', False),
)


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


THING_SETTINGS = {
    'Defence': (0, 10),
    'AttackPoints': (5, 15),
    'Hp': (30, 50),
}
PERSON_SETTINGS = {
    'Defence': (15, 30),
    'AttackPoints': (20, 30),
    'Hp': (220, 300),
}