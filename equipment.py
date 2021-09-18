__all__ = ['equipments']

class Armor:

    def __init__(self, name: str, armor: float, *args, **kwargs) -> None:
        self.name: str = name
        self.armor = armor
        super().__init__(*args, **kwargs)

    def __str__(self):
        return  self.name


class Shield(Armor):

    def __init__(self, name, block_chance: float, armor: float, *args, **kwargs):
        self.block_chance = block_chance
        super().__init__(name, armor, *args, **kwargs)

    def __repr__(self):
        return f'{self.name}'


class Chest(Armor):

    def __init__(self, name, hp, armor: float, *args, **kwargs):
        self.hp = hp
        super().__init__(name, armor, *args, **kwargs)

    def __repr__(self):
        return f'{self.name}'


class Weapon:
    def __init__(self, name: str, damage: float, *args, **kwargs):
        self.name: str = name
        self.damage: float = damage
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name


class Sword(Weapon):

    def __init__(self, name: str, ignore_armor: float, damage: float, *args, **kwargs):
        self.ignore_armor: float = ignore_armor
        super().__init__(name, damage, *args, **kwargs)

    def __repr__(self):
        return f'{self.name}'


class Dagger(Weapon):

    def __init__(self, name: str, damage: float, crit_chance: float, *args, **kwargs):
        self.crit_chance: float = crit_chance
        super().__init__(name, damage, *args, **kwargs)

    def __repr__(self):
        return f'{self.name}'


sword_1 = Sword(name='Палка', ignore_armor=0.5, damage=7)
sword_2 = Sword(name='Молоток', ignore_armor=1, damage=12)
sword_3 = Sword(name='Добротный меч', ignore_armor=2, damage=12)
sword_4 = Dagger(name='Вилка', damage=4, crit_chance=4)
sword_5 = Dagger(name='Ядовитый кинжал', damage=9, crit_chance=8)
sword_6 = Dagger(name='Перочинный нож', damage=7, crit_chance=3)
shield_1 = Shield(name='Круглый щит', block_chance=4, armor=0.13)
shield_2 = Shield(name='Башенный щит', block_chance=7, armor=0.17)
chest_1 = Chest(name='Тельняжка', armor=12, hp=30)
chest_2 = Chest(name='Тяжелый доспех', armor=0.15, hp=60)
chest_3 = Chest(name='Модная кожанка', armor=0.10, hp=70)

equipments = [sword_1, sword_2, sword_3, sword_4, sword_5, sword_6, shield_1, shield_2, chest_1, chest_2, chest_3]
