from battle import fight_with_map
from other_utils import create_stuff, create_percs, equip_percs
import colorama

if __name__ == "__main__":
    colorama.init()
    items = create_stuff()
    percs = create_percs(count=10)
    equip_percs(percs, items)
    fight_with_map(percs, 0.3)
    print(20 * '- ')
    print(percs[0])
