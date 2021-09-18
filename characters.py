class Person:
    """Базовый класс для персонажа."""

    def __init__(self, name, hp, base_attack, base_defence, things=None):
        self.name = name
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.hp = hp
        self.things = things

    def set_things(self, thing_inst):
        """Доабвить предмет в инвентарь."""
        self.things.append(thing_inst)

    @property
    def final_attack(self):
        """Получить значение урона с учетом предметов."""
        attack_damage = self.base_attack
        if self.things:
            for thing in self.things:
                attack_damage += thing.attack
        return attack_damage

    @property
    def final_defence(self):
        """Получить параметры защиты с учетом предметов."""
        defence = self.base_defence
        if self.things:
            for thing in self.things:
                defence += thing.defence
        return round(defence, 2)

    def set_final_hp(self):
        """Установить здоровье с учетом предметов."""
        hp = self.hp
        if self.things:
            for thing in self.things:
                self.hp += thing.hp
        return hp


class Paladin(Person):
    """Класс паладин в два раза больше здоровья."""
    def __init__(self, name, hp, base_attack, base_defence, things):
        super().__init__(name, hp * 2, base_attack, base_defence * 2, things)


class Warrior(Person):
    """Клаcс Warrior в два раза больше атака."""
    def __init__(self, name, hp, base_attack, base_defence, things):
        super().__init__(name, hp, base_attack * 2, base_defence, things)


class Dwarf(Person):
    """Класс dwarf, в два раза больше здоровья и защиты, но в 2 раза меньше атака."""
    def __init__(self, name, hp, base_attack, base_defence, things):
        super().__init__(name, hp * 2, base_attack / 2, base_defence * 2, things)
