from random import shuffle, randint, choice

from oophack.things import Thing
from other_utils import create_stuff, create_percs, equip_percs
from person import Person
from specialization import Paladin, Warrior

if __name__ == "__main__":
    items = create_stuff()
    percs = create_percs(count=10)
    equip_percs(percs, items)

    print(percs[0])
    for _ in percs[0].get_person_items():
        print(_.get_feature())

    # print(items[0].get_feature())
    # [print(item) for item in items]


    # pers1 = Person('Генерал-адмирал Алладин', attack=70, defense=0.02, hp=500)
    # pers2 = Person('Дамблдор', attack=60, defense=0.07, hp=350)
    #
    # pers1.set_things([thing_1, thing_2])
    # print(pers1)
    # pers2.set_things([thing_3])
    # print(pers2)
    #
    # while pers1.final_hp > 0 and pers2.final_hp > 0:
    #     pers1.under_attack(pers2)
    #     if pers1.final_hp == 0:
    #         break
    #     pers2.under_attack(pers1)

    # pal = Paladin('Артас', attack=60, defense=0.07, hp=600)
    # print(pal)
    # war = Warrior('Гаррош', attack=70, defense=0.07, hp=600)
    # print(war)
