'''Зась задается список вещей.'''
from classes import Thing
# Словарь имен вещей и их характеристикв порядке 
# protection, attack, life. Поле со значением None
# задается рандомно
# protection от 0% до 0.1%
# attack от 0 до 10
# life от 0 до 100 с шагом 10
names_of_things = {'ring': [None, None, None], 
                   'sword': [None, None, None], 
                   'spear': [None, None, None], 
                   'saber': [None, None, None], 
                   'mace': [None, None, None], 
                   'pikestaff': [None, None, None], 
                   'helmet': [None, None, None], 
                   'belt': [None, None, None], 
                   'chain_mail': [None, None, None], 
                   'bracers': [None, None, None], 
                   'leggings': [None, None, None],}
# Здесь будет храниться список вещей
things = []
# создаем произвольное количество вещей с различными параметрами
for thing in names_of_things:
    things.append(Thing(thing, *names_of_things[thing]))
# Сортируем по проценту защиты, по возрастанию
things.sort(key=lambda thing: thing.protection)
