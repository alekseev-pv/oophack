"""
Мини-проект "игра-арена"

Игра арена, на которую вы выпустите своих персонажей
и заставите их сражаться между собой. Играющая сама в себя
и выдающая вам только результат своей работы.

"""

from colorama import init

from functions import arena, create_heroes, create_things, dress_heroes

if __name__ == "__main__":
    init()

    things = create_things()
    heroes = create_heroes()
    dress_heroes(heroes, things)
    arena(heroes)
