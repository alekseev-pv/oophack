from __future__ import annotations
import random
from typing import Union, List

from equipment import equipments, Dagger, Sword, Chest, Shield


class Person:

    def __init__(self, name: str, *args, **kwargs) -> None:
        # all person start with default attack, protect,  hp
        self.name: str = name
        self.hp: float = 100
        self.damage: float = 5
        self.armor: float = 0.2
        self.sword: int = 0
        self.shield: int = 0
        self.chest: int = 0
        self.dagger: int = 0


class Paladin(Person):
    armor_bonus: int = 2

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.block_chance: float = 0
        self.ignore_armor: float = 0

        super().__init__(name, *args, **kwargs)

    def equip(self, equipment: List[Union[Dagger, Sword, Chest, Shield]]) -> None:
        # paladin cant wear dagger
        if isinstance(equipment, Dagger):
            print(f'{self.name} вертит в руке {equipment.name}: что за хренатень?! как я должен использовать эту штуку?!?!')
        # if shield
        elif isinstance(equipment, Shield) and self.shield == 0:
            print(f'{self.name} хватает {equipment.name}: отличная штука! как за каменной стеной')
            self.armor += equipment.armor * Paladin.armor_bonus
            self.block_chance = equipment.block_chance
            self.shield = 1
        # if sword
        elif isinstance(equipment, Sword) and self.sword == 0:
            print(f'{self.name} поднимает вверх {equipment.name}: свет да испепелит тьму!')
            self.damage += equipment.damage
            self.ignore_armor = equipment.ignore_armor
            self.sword = 1
        elif isinstance(equipment, Chest) and self.chest == 0:
            print(f'{self.name} с трудом надевая {equipment.name}: а нет ли размерчика побольше?')
            self.hp += equipment.hp
            self.armor += equipment.armor * Paladin.armor_bonus
            self.chest = 1

    def character_characteristics(self) -> dict:
        return {'hp': self.hp, 'damage': self.damage, 'armor': self.armor,
                'block_chance': self.block_chance, 'ignore_armor': self.ignore_armor}

    def __repr__(self) -> str:
        return f'бронированный с ног до головы паладин {self.name}'


class Warrior(Person):
    hp_bonus: float = 1.5

    def __init__(self, name: str, *args, **kwargs):
        self.block_chance: float = 0
        self.ignore_armor: float = 0
        self.crit_chance: float = 0
        super().__init__(name, *args, **kwargs)

    def equip(self, equipment: Union[Dagger, Sword, Chest, Shield]) -> None:
        if isinstance(equipment, Dagger) and self.dagger == 0 and self.sword == 0:
            print(f'{self.name} поднимает {equipment.name}: хотелось бы что-то помассивнее... но сойдет и это')
            self.dagger = 1
            self.crit_chance += equipment.crit_chance
            self.damage += equipment.damage
        # if shield
        elif isinstance(equipment, Shield) and self.shield == 0:
            print(f'{self.name} осматривая {equipment.name}: отличная штука! будет на чем в картишки перекинуться'
                  f'после заварушки')
            self.armor += equipment.armor * Paladin.armor_bonus
            self.block_chance = equipment.block_chance
            self.shield = 1
        # if sword
        elif isinstance(equipment, Sword) and self.dagger == 0 and self.sword == 0:
            print(f'{self.name} хватает {equipment.name}: крушиииииить!')
            self.damage += equipment.damage
            self.ignore_armor = equipment.ignore_armor
            self.sword = 1
        elif isinstance(equipment, Chest) and self.chest == 0:
            print(f'{self.name} надевая {equipment.name}: в самый раз!')
            self.hp += equipment.hp * Warrior.hp_bonus
            self.chest = 1

    def character_characteristics(self) -> dict:
        return {'hp': self.hp, 'damage': self.damage, 'armor': self.armor,
                'block_chance': self.block_chance, 'ignore_armor': self.ignore_armor, 'crit_chance': self.crit_chance}

    def __repr__(self) -> str:
        return f'яростный воин {self.name}'


class Rogue(Person):
    damage_bonus: float = 2.0
    miss_chance: float = 2.0
    equip_shield: bool = False

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.ignore_armor: float = 0
        self.crit_chance: float = 0
        super().__init__(name, *args, **kwargs)

    def equip(self, equipment: List[Union[Dagger, Sword, Chest, Shield]]) -> None:
        if isinstance(equipment, Dagger) and self.dagger == 0 and self.sword == 0:
            if {equipment.name} == 'Вилка':
                print(f'{self.name} поднимает {equipment.name}: отлично! один удар - четыре дырки...')
            else:
                print(f'{self.name} поднимает {equipment.name}: сколько я зарезал, скооолько перерезал')
            self.dagger = 1
            self.crit_chance += equipment.crit_chance
            self.damage += equipment.damage * Rogue.damage_bonus
        elif isinstance(equipment, Shield):
            print(f'{self.name} осматривая {equipment.name}: это мне не понадобится')
        # if sword
        elif isinstance(equipment, Sword) and self.sword == 0:
            print(f'{self.name} озираясь по сторонам, берет {equipment.name}: хотелось бы что-нибудь поизящнее!')
            self.damage += equipment.damage * Rogue.damage_bonus
            self.ignore_armor = equipment.ignore_armor
            self.sword = 1
        elif isinstance(equipment, Chest) and self.chest == 0:
            print(f'{self.name} надевая {equipment.name}: погнааали!!')
            self.hp += equipment.hp
            self.chest = 1

    def character_characteristics(self) -> dict:
        return {'hp': self.hp, 'damage': self.damage, 'armor': self.armor,
                'block_chance': Rogue.miss_chance, 'ignore_armor': self.ignore_armor, 'crit_chance': self.crit_chance}

    def __repr__(self) -> str:
        return f'хитрый как скорпион убийца {self.name}'


class Arena:

    def __init__(self, equipments: List[Union[Dagger, Sword, Chest, Shield]],
                 characters: List[Union[Warrior, Rogue, Paladin]]) -> None:
        self.characters: List[Union[Warrior, Rogue, Paladin]] = characters
        self.equipments: List[Union[Dagger, Sword, Chest, Shield]] = equipments

    def dress_up_characters(self) -> None:
        equipments: List[Union[Dagger, Sword, Chest, Shield]] = self.equipments[:]
        equipment_count: int = len(self.equipments)
        i: int = 0
        for character in self.characters:
            equipped: list = []
            while i != 4:
                equipment_index = random.randint(0, equipment_count - 1)
                character.equip(equipments[equipment_index])
                del equipments[equipment_index]
                equipment_count = len(equipments)
                i += 1
            i = 0

    def introduce_faiters(self) -> None:
        print(f'В левом углу  {self.characters[0]}')
        char1_characteristic = self.characters[0].character_characteristics()
        print(char1_characteristic)
        print(f'В правом углу  {self.characters[1]}')
        char2_characteristic = self.characters[1].character_characteristics()
        print(char2_characteristic)
        print(f'Fait!!!')

    def fait(self) -> None:
        i: int = 0
        while self.characters[0].hp >= 0 or self.characters[1].hp >= 0:
            print(f'{i + 1} ход')
            print(f'{self.characters[0].name} наносит удар')
            self.characters[1].hp = self.characters[1].hp - self.characters[0].damage * (1 - self.characters[1].armor)
            if self.characters[1].hp <= 0:
                return print(f'слава победителю! Ура {self.characters[0].name}')

            print(f'{self.characters[1].name} не остается в долгу')
            self.characters[0].hp = self.characters[0].hp - (self.characters[1].damage -
                                                             self.characters[1].damage * self.characters[0].armor)
            if self.characters[0].hp <= 0:
                return print(f'слава победителю! Ура {self.characters[1].name}')
            print(self.characters[0].hp)
            print(self.characters[1].hp)
            i += 1


if __name__ == '__main__':
    equipment = ', '.join(str(i) for i in equipments)
    print(f'вам может повезти и вы получите одну из следующих вещей:\n'
          f'{equipment} \n')

    paladin = Paladin('Антоха')
    warrior = Warrior('Иван')
    rogue = Rogue('Никитос')

    characters = [paladin, rogue]
    arena = Arena(equipments=equipments, characters=characters)
    arena.dress_up_characters()
    arena.introduce_faiters()
    arena.fait()
