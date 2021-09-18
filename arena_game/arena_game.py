from units import *


class Game:

    def __init__(self):
        self.things = self.make_things()
        self.players = self.__set_warriors()

    def make_things(self):
        amount = random.randint(1, len(THINGS))
        names = random.sample(THINGS, amount)
        return sorted([Thing(name=name,
                      protection=round(random.random()/10, 2))
                      for name in names])

    def __set_warriors(self):
        players = []
        players_list = random.sample(PERSONS, AMOUNT_OF_PLAYERS)
        for player in players_list:
            new_player = select_race(player)
            new_player.set_things(self.things)
            players.append(new_player)
        return players

    @staticmethod
    def __hit_defender(attacker, defender):
        damage = round(attacker.attack_damage * (1 - defender.finalProtection), 2)
        defender.HitPoints = round(defender.HitPoints - damage, 2)
        return f'{attacker} наносит удар по {defender} на {damage} hp'

    @staticmethod
    def __get_defender_status(defender):
        return f'{defender} после атаки: {defender.HitPoints} hp'

    def __game_round(self, N):
        print(f'\n============== РАУНД {N} ===================')
        attacker, defender = random.sample(self.players, 2)
        print(self.__hit_defender(attacker, defender))
        print(self.__get_defender_status(defender))
        if defender.HitPoints <= 0 and defender in self.players:
            print(f'{defender} выбывает')
            del self.players[self.players.index(defender)]

    def play(self):
        N = 1
        while len(self.players) > 1:
            self.__game_round(N)
            N += 1
        print(f'\n============== КОНЕЦ ИГРЫ ===================')
        print(f'======= ПОБЕДИТЕЛЬ - {self.players[0]} ========')


if __name__ == '__main__':
    G = Game()
    G.play()
