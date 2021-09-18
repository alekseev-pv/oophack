import curses
import time
from typing import List

from colorama import Back, Fore, Style

from other_utils import map_spec_icons
from person import Person


def draw_all_percs(
        attacker: Person,
        victim: Person,
        percs: List[Person],
        speed):
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

    def print_xy(x, y, message, color):
        # Draw the text
        screen.addstr(x, y, message, color)

    px, py = 4, 2
    ix, iy = 1, 100
    color = curses.color_pair(1)
    print_xy(ix, iy, "INFO:", color)
    for perc in percs:
        ix += 1
        if perc != attacker and perc != victim:
            color_name = (f'{perc.spec_name} - {perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            color = curses.color_pair(2)
            print_xy(ix, iy, color_name, color)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon, color)
        elif perc == attacker:
            mes = (f'ATTACKER - {perc.spec_name} - '
                          f'{perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            color = curses.color_pair(3)
            print_xy(ix, iy - 11, mes, color)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon, color)
        else:
            mes = (f'VICTIM - {perc.spec_name} - '
                          f'{perc.name}: '
                          f'hp = {perc.final_hp}, '
                          f'attack = {perc.final_attack}')
            color = curses.color_pair(4)
            print_xy(ix, iy - 9, mes, color)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            icon = map_spec_icons[perc.spec_name]
            print_xy(x, y, icon, color)
    screen.refresh()
    time.sleep(speed)
    screen.clear()

    # Wait and cleanup
    # curses.napms(1000)
    curses.endwin()
