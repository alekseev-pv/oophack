class Thing:

    def __init__(self, thing_name, t_attack=None, t_deff=None, t_hp=None):
        self.thing_name = thing_name
        self.t_deff = t_deff
        self.t_attack = t_attack
        self.t_hp = t_hp
        print(f'Создан предмет "{self.thing_name}"')

    def __str__(self):
        return self.thing_name
