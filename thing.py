class Thing:
    def __init__(self, name, hp, attack_power, protection):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.protection = protection
        print(f'Предмет {self.name} создан')
