import curses
import time
from typing import List

from other_utils import map_spec_icons
from person import Person


def draw_all_percs(
        attacker: Person,
        victim: Person,
        percs: List[Person],
        speed):
    screen = curses.initscr()

    def print_xy(x, y, message):
        # Draw the text
        screen.addstr(x, y, message)

    px, py = 4, 2
    ix, iy = 1, 100
    print_xy(ix, iy, "INFO:")
    for perc in percs:
        # TODO(color for map and info table)
        ix += 1
        if perc != attacker and perc != victim:
            color_name = (f'{perc.spec_name} - {perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            print_xy(ix, iy, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon)
        elif perc == attacker:
            color_name = (f'ATTACKER - {perc.spec_name} - '
                          f'{perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            print_xy(ix, iy - 11, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon)
        else:
            color_name = (f'VICTIM - {perc.spec_name} - '
                          f'{perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            print_xy(ix, iy - 9, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon)
    screen.refresh()
    time.sleep(speed)
    screen.clear()

    # Wait and cleanup
    # curses.napms(1000)
    curses.endwin()
