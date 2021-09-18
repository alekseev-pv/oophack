from characters import Person


class Paladin(Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.hp = hp * 2
        self.protection = base_protection * 2
        print(f'Явился новый воин Альянса!\n   Дитя света -  {self}')

# Сделаю по мативам Вов классик))
# class Warrior(Person):
class Shaman(Person):
    def __init__(self, name: str, hp: int, base_atack: int, base_protection: int):
        super().__init__(name, hp, base_atack, base_protection)
        self.atack = base_atack * 2
        # Шаман критует на 10 проц чаще
        self.crit += 10 
        print(f'Явился новый воин Орды!\n   Shaman {self}  Сам Вождь благославил его на бой!')
