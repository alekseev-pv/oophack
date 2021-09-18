from items import Thing
from character import Paladin, Warrior
from typing import List
from random import randint, randrange
from operator import attrgetter
import colorama
from colorama import Fore, Back, Style

ITEM_NAMES = [
    "metal sword",
    "metal ring",
    "metal shield",
    "metal arms",
    "metal boots",
    "copper sword",
    "copper ring",
    "copper shield",
    "copper arms",
    "copper boots",
    "golden sword",
    "golden ring",
    "golden shield",
    "golden arms",
    "golden boots",
    "platinum sword",
    "platinum ring",
    "platinum shield",
    "platinum arms",
    "platinum boots",
    "wooden arrow",
    "metal mace",
    "golden mace",
    "platinum mace",
    "metal axe",
    "platinum axe",
    "golden axe",
    "metal spear",
]

CHARACTER_NAMES = [
    "Liam",
    "Noah",
    "Oliver",
    "Elijah",
    "William",
    "James",
    "Benjamin",
    "Lucas",
    "Henry",
    "Alexander",
    "Olivia",
    "Emma",
    "Ava",
    "Charlotte",
    "Sophia",
    "Amelia",
    "Isabella",
    "Mia",
    "Evelyn",
    "Harper",
]


class GameLoop:
    def __init__(self) -> None:
        self.things = self.__create_items()
        self.players = self.__create_players()
        self.__set_things_on_players()
        colorama.init()

    def __create_items(self) -> List[Thing]:
        res: List[Thing] = []

        for i in range(randrange(0, len(ITEM_NAMES))):
            res.append(
                Thing(
                    ITEM_NAMES[i],
                    randint(1, 10),
                    randint(10, 100),
                    randint(0, 50),
                )
            )

        return sorted(res, key=attrgetter("defense"))

    def __create_players(self) -> []:
        res = []

        for _ in range(0, 10):
            num = randint(0, 1)
            name_res = CHARACTER_NAMES[randint(0, len(CHARACTER_NAMES) - 1)]
            hp_res = randint(100, 500)
            attack_res = randint(100, 150)
            defense_res = randint(5, 50)

            if num == 0:
                res.append(
                    Warrior(
                        "Warrior " + name_res, hp_res, attack_res, defense_res
                    )
                )
            else:
                res.append(
                    Paladin(
                        "Paladin " + name_res, hp_res, attack_res, defense_res
                    )
                )

        return res

    def __set_things_on_players(self) -> None:
        for player in self.players:
            things_for_player = []
            for _ in range(randrange(1, 5)):
                things_for_player.append(
                    self.things[randint(0, len(self.things) - 1)]
                )

            player.set_things(things_for_player)

    def __pop_defender(self):
        return self.players.pop(randint(0, len(self.players) - 1))

    def __get_attacker(self):
        return self.players[randint(0, len(self.players) - 1)]

    def start(self) -> None:
        while True:
            attacker = self.__get_attacker()
            defender = self.__pop_defender()

            defender.receive_attack(attacker)

            if defender.hp > 0:
                self.players.append(defender)
            else:
                print(Fore.RED + f"{defender.name} умер" + Style.RESET_ALL)

            if len(self.players) == 1:
                print(Fore.BLACK + Back.WHITE + "Игра окончена")
                print(f"Победитель {self.players[0].name}")

                return
