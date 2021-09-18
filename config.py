# импортируем библиотеку с пресетами в конфиг, а в main.py берем config.presets
from presets.starwars import presets

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
GENERAL_SETTINGS = {
    'WarriorsCount': 10,
    'MaximumGearInOneHand': 4
}
