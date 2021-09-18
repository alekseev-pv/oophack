class Thing:
    def __init__(self, name: str, attack: int, defense: float, hp: int):
        self.name = name
        self.defense = round(defense, 2)
        if self.defense > 0.1:
            self.defense = 0.1
        self.attack = round(attack)
        self.hp = hp

    # можно добавить тип куда надевается,
    # одноручное, двуручное, кольца (не более 10)
    # что на шею, щит
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'"{self.name}"'

    def get_feature(self):
        out = (f'Вещь - {self.name}:\n'
               f'атака -> {self.attack}\n'
               f'защита -> {self.defense}\n'
               f'здоровье -> {self.hp}' + '\n' + 20 * '- ')
        return out
