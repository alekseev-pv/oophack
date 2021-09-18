from main_classes import Thing

THING_LIBRARY = {
    1: Thing(name='Кольцо силы', bonus_attack=15),
    2: Thing(name='Кольцо защиты', bonus_defense=10),
    3: Thing(name='Кольцо ловкого воина', bonus_dodge=20, bonus_block=20),
    4: Thing(name='Кольцо бычьего здоровья', bonus_health=20),
    5: Thing(name='Точильный камень', bonus_attack=20),
    6: Thing(name='Статуэтка танцовщицы', bonus_dodge=25),
    7: Thing(name='Ростовой щит', bonus_block=20, bonus_defense=20),
    8: Thing(name='Облегченные доспехи школы Кота', bonus_dodge=20,
             bonus_defense=-10),
    9: Thing(name='Доспехи школы Медведя', bonus_defense=20),
    10: Thing(name='Камень жизни', bonus_health=20),
}
