class Thing():
    """Родитель вещей"""

    def __init__(self, name, defence_mod=None, attack_mod=None, health_mod=None):
        self.name = name
        self.defence_mod = defence_mod
        self.attack_mod = attack_mod
        self.health_mod = health_mod
        print(f'Создан {self.name}')