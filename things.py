class Thing:
    """Класс представление магического предмета."""
    def __init__(self, name, defence, attack, hp):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp

    @property
    def defence(self):
        """Получить бонус к защите."""
        return self._defence

    @defence.setter
    def defence(self, value):
        """Установить бонус к защите."""
        if value > 0.1:
            raise ValueError('Защита не может быть больше 10')
        else:
            self._defence = value
