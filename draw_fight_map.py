import time
import curses
from typing import List

from colorama import Back, Fore, Style

from person import Person


def draw_all_percs(attacker: Person, victim: Person, percs: List[Person], speed):
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
            color_name = f'{perc.name}: hp = {perc.final_hp}, attack = {perc.final_attack}'
            print_xy(ix, iy, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            print_xy(x, y, "O")
        elif perc == attacker:
            color_name = f'ATTACKER - {perc.name}: hp = {perc.final_hp}, attack = {perc.final_attack}'
            print_xy(ix, iy - 11, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            print_xy(x, y, "A")
        else:
            color_name = f'VICTIM - {perc.name}: hp = {perc.final_hp}, attack = {perc.final_attack}'
            print_xy(ix , iy - 9, color_name)
            x = int((perc.point[0] / px))
            y = int((perc.point[1] / py))
            print_xy(x, y, "V")
        screen.refresh()
    time.sleep(speed)
    screen.clear()

    # Wait and cleanup
    # curses.napms(1000)
    curses.endwin()
