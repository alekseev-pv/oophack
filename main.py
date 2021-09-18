from battle import start_fight
from other_utils import create_stuff, create_percs, equip_percs
import colorama

if __name__ == "__main__":
    colorama.init()
    items = create_stuff()
    percs = create_percs(count=2)
    equip_percs(percs, items)
    start_fight(percs)
    print(20 * '- ')
    print(percs[0])
