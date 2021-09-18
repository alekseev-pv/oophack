
class Person:
    def __init__(self, name, attack, defense, hp):
        self.things = []
        self.spec_name = 'No class'
        self.name = name
        self.final_hp = hp
        self.final_protection = round(defense, 2)
        self.final_attack = round(attack)
        print(f'Персонаж {self.name} создан!')

    def __str__(self):
        person_out = (f'{self.name} - {self.spec_name}\n'
                      f'атака: {self.final_attack}\n'
                      f'защита: {self.final_protection}\n'
                      f'здоровье: {self.final_hp}' + '\n' + 20 * '- ')
        return person_out

    def set_things(self, things, print_out=False):
        self.things = things[:3]
        for thing in self.things:
            self.final_hp += thing.hp
            self.final_protection = round(self.final_protection + thing.defense, 2)
            self.final_attack += thing.attack
            if print_out:
                print(f'{self.name} с гордостью надевает: {thing.name}' + '\n' + 20 * '- ')  # "с гордостью надевает" -> beautify_wear

    def drop_things(self):
        pass

    def under_attack(self, attacker):
        '''
        :param attacker: class Person
        :return: nothing
        '''
        self.final_hp = round(self.final_hp - attacker.final_attack * (1 - self.final_protection))
        if self.final_hp <= 0:
            self.final_hp = 0
            print(f'{self.name} повержен!')
        else:
            # можно добавить другие фразы в зависимости от оставшегося хп, входящего и фактически нанесенного урона
            print(f'У {self.name} осталось {self.final_hp}')

    def get_person_items(self):
        return self.things