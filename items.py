class Thing:
    def __init__(self, name: str, defense: int, attack: int, hp: int) -> None:
        self.name = name
        self.defense = float(defense / 100)
        self.attack = attack
        self.hp = hp
