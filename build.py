class Thing:
    def __init__(self, name, protection, power, life,):
        self.name = name
        self.protection = protection
        self.power = power
        self.life = life

    def __repr__(self):
        return f'{self.name}'


class Person:
    def __init__(self, name, base_protection, power_base, life,):
        self.name = name
        self.final_protection = base_protection
        self.final_power = power_base
        self.life = life

    def set_things(self, things):
        self.things = things
        for thing in things:
            self.final_protection += thing.protection
            self.final_power += thing.power

    def get_hit(self, person):
        pass

    def __repr__(self):
        return (f'{self.__class__.__name__}({self.name}: '
                f'{self.final_protection},{self.final_power},{self.life})'
                # f'{self.things}'
                )


class Paladin(Person):
    def __init__(self, name, base_protection, power_base, life,):
        super().__init__(name, base_protection, power_base, life,)
        self.life *= 2
        self.final_protection *= 2


class Warrior(Person):
    def __init__(self, name, immunity_base, power_base, life,):
        super().__init__(name, immunity_base, power_base, life,)
        self.final_power *= 2
