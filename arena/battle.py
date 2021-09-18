"""Основной файл проекта."""

import random
from gladiators import the_participants

# В цикле в произвольном порядке выбирается пара Нападающий и Защищающийся.
# Цикл идет до тех пор, пока не останется последнего выжившего
while len(the_participants) != 1:
    # Защищающийся выбирается из основрого списка персонажей
    defender = random.choice(the_participants)
    # Создаем копию основрого списка персонажей и удаляем из него
    # Защищающегося для того, чтобы Нападающий и Защищающийся не оказался
    # одним и тем же персонажем
    the_participants_copy = the_participants.copy()
    the_participants_copy.remove(defender)
    # Нападающий выбирается из копии списка персонажей
    attacking = random.choice(the_participants_copy)
    # Отправляем персонажей на арену
    print(f'На арену выходят {defender} и {attacking}')
    # У Защищающегося вызывается метод вычитания жизни на основе атаки
    # `(attack_damage)` Нападающего
    defender.take_away(attacking)
    # Если у Защищающегося не осталось НР, исключаем его из списка участников
    if defender.final_hit_points <= 0:
        the_participants.remove(defender)
        print(f'{defender} выбывает из соревнования')
        print()

print(f'И победителем арены стаовится {the_participants[0]}!!!')
