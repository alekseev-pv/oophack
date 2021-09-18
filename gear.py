ONE = 1
PCT_MAX = 100
MAX_PROTECTION = MAX_ATACK = 10
MAX_CRIT = MAX_PRECISION = 20
MAX_ADD_HP = 20


class Thing:
    ''' Всякий инвентарь'''
    def __init__(self, name: str, protection: int, damage: int, add_hp: int, precision: int, crit: int):
        assert ONE <= protection <= MAX_PROTECTION, f'Защита не более {MAX_PROTECTION}'
        assert ONE <= damage <= MAX_ATACK, f'Атака не более {MAX_ATACK}'
        assert ONE <= add_hp <= MAX_ADD_HP, f'Добавляем не более {MAX_ADD_HP} HP'
        assert ONE <= precision <= MAX_PRECISION, f'Точность должна быть не более {MAX_PRECISION}'
        assert ONE <= crit <= MAX_CRIT, f'Крит не более {MAX_CRIT}'
        self.name = name
        self.protection = protection
        self.damage = damage
        self.add_hp = add_hp
        self.precision = precision
        self.crit = crit

    def __str__(self) -> str:
        return f'Экипировано {self.name}!'