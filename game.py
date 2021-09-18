import random

CHAR_NAME_LIST = [i for i in range(1, 21)]

THINGS_NAMES = ['кольцо', 'посох', 'волшебная палочка', 'плащ', 'посох']


class Thing:
    def __init__(self, name, defence, attack, hp):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.lives = hp

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        if value > 0.1:
            raise ValueError('Защита не может быть больше 10')
        else:
            self._defence = value


class Person:
    def __init__(self, name, hp, base_attack, base_defence, things):
        self.name = name
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.hp = hp
        self.things = things

    def set_things(self, thing_inst):
        self.things.append(thing_inst)

    def get_final_attack(self):
        attack_damage = self.base_attack
        if self.things:
            for thing in self.things:
                attack_damage += thing.attack
        return attack_damage

    def get_final_defence(self):
        defence = self.base_defence
        if self.things:
            for thing in self.things:
                defence += thing.defence
        return defence


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_defence, things):
        super().__init__(name, hp * 2, base_attack, base_defence * 2, things)


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_defence, things):
        super().__init__(name, hp, base_attack * 2, base_defence, things)


class Arena:
    def __init__(self):
        self.team1 = []
        self.team2 = []
        self.things = []

    def _add_to_team1(self, obj):
        self.team1.append(obj)

    def _add_to_team2(self, obj):
        self.team2.append(obj)

    def _generate_random_character(self, available_characters_list):
        char = random.choice(available_characters_list)
        things = []
        if self.things:
            things = random.choices(self.things, k=random.randint(0, 4))
        new_char = char(
            name=random.choice(CHAR_NAME_LIST),
            hp=100,
            base_attack=random.randint(1, 10),
            base_defence=random.uniform(0.01, 0.3),
            things=things
        )
        return new_char

    def generate_random_thing(self, Thing):
        for _ in range(random.randint(1, 100)):
            new_thing = Thing(
                name=random.choice(THINGS_NAMES),
                defence=random.uniform(0.001, 0.1),
                attack=random.randint(0, 3),
                hp=1
            )
            self.things.append(new_thing)

    def generate_characters(self, available_characters_list):
        for _ in range(10):
            new_char = self._generate_random_character(
                available_characters_list)
            self._add_to_team1(new_char)
        for _ in range(10):
            new_char = self._generate_random_character(
                available_characters_list)
            self._add_to_team2(new_char)

    def game_round(self, attacker, defender):
        attack_damage = attacker.get_final_attack()
        final_defence = defender.get_final_defence()
        final_damage = attack_damage - attack_damage * final_defence
        final_damage = round(final_damage, 2)
        defender.hp -= final_damage
        print(
            f'Персонаж {attacker.name} наносит урон {final_damage} персонажу {defender.name}')

    def is_over(self):
        if not self.team1:
            print('Победа за командой 2')
            return True
        if not self.team2:
            print('Победа за командой 1')
            return True
        return False





def main():
    active = True
    arena = Arena()
    arena.generate_random_thing(Thing)
    arena.generate_characters([Warrior, Paladin])
    while active:
        attacker = random.choice(arena.team1)
        defender = arena.team2.pop(random.randint(0, len(arena.team2) - 1))
        arena.game_round(attacker, defender)
        if defender.hp > 0:
            arena.team2.append(defender)
        if arena.is_over():
            break
        attacker = random.choice(arena.team2)
        defender = arena.team1.pop(random.randint(0, len(arena.team1) - 1))
        arena.game_round(attacker, defender)
        if defender.hp > 0:
            arena.team1.append(defender)
        if arena.is_over():
            break


if __name__ == '__main__':
    main()
