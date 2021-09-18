import random
from time import sleep
from typing import List


class Thing:
    """Класс вещи. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points),
    - признак оружия (is_weapon),
    - признак одежды (is_clothes)."""
    name: str
    defence_percent: int
    attack_points: float
    health_points: float
    is_weapon: bool
    is_clothes: bool

    def __init__(self, name, defence_percent, attack_points, health_points,
                 is_weapon, is_clothes):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points
        self.is_weapon = is_weapon
        self.is_clothes = is_clothes

    def decrease_health_points(self, attack_damage):
        if self.health_points < attack_damage:
            difference = attack_damage - self.health_points
            self.health_points = 0
            return difference

        self.health_points -= attack_damage

        return None


class Person:
    """Класс персонажа. На вход принимает:
    - имя (name),
    - процент защиты (defence_percent),
    - количество атаки (attack_points),
    - количество жизней (health_points)."""
    name: str
    defence_percent: int
    final_protection: float
    health_points: float
    attack_points: float
    is_unique: bool
    things: List[Thing]

    def __init__(self, name, defence_percent, attack_points, health_points,
                 is_unique, skills=None):
        self.name = name
        self.defence_percent = defence_percent
        self.attack_points = attack_points
        self.health_points = health_points
        self.is_unique = is_unique

        self.attack_skills = []
        self.defend_skills = []

        if skills:
            for skill in skills:
                if skill.get('is_attack', False):
                    self.attack_skills.append(skill)
                else:
                    self.defend_skills.append(skill)

        self.__recalculate_final_protection()

    def __total_points(self, attrname):
        """Вычисление количества поинтов (атрибут передается в attrname)
        экземпляра."""
        points = getattr(self, attrname)
        try:
            points += sum([getattr(thing, attrname) for thing in self.things])
        except AttributeError:
            pass

        return points

    def __recalculate_final_protection(self):
        self.final_protection = self.total_defence_percent() / 100

    def set_things(self, things):
        """Устанавливаем список вещей."""
        self.things = things
        self.__recalculate_final_protection()

    def remove_thing(self, thing):
        self.things.pop(self.things.index(thing))
        self.__recalculate_final_protection()

    def decrease_health_points(self, attack_damage):
        """Метод вычитания health_points экземпляра в зависимости от атаки
        attack_damage."""
        damage = attack_damage

        # сперва снимаем HP со снаряжения
        if self.things:
            things_to_remove = []
            for thing in self.things:
                damage = thing.decrease_health_points(damage)
                if damage is None:
                    break
                things_to_remove.append(thing)

            if things_to_remove:
                list(map(self.things.remove, things_to_remove))

        if damage is None:
            damage = 0

        health_points = self.health_points - damage
        self.health_points = 0 if health_points < 0 else health_points

    def total_defence_percent(self):
        """Вычисление количества поинтов защиты."""
        return self.__total_points('defence_percent')

    def total_attack_points(self):
        """Вычисление количества поинтов атаки."""
        return self.__total_points('attack_points')

    def total_health_points(self):
        """Вычисление количества поинтов здоровья."""
        return self.__total_points('health_points')

    def total_final_protection(self):
        return self.final_protection


class Paladin(Person):
    """Класс Паладина. Наследуется от Person."""

    warrior_type = 'Паладин'

    def __init__(self, name, defence_percent, attack_points, health_points,
                 is_unique, skills):
        super().__init__(name, defence_percent, attack_points, health_points,
                         is_unique, skills)

        self.health_points *= 2
        self.defence_percent *= 2


class Warrior(Person):
    """Класс Воина. Наследуется от Person."""

    warrior_type = 'Воин'

    def __init__(self, name, defence_percent, attack_points, health_points,
                 is_unique, skills):
        super().__init__(name, defence_percent, attack_points, health_points,
                         is_unique, skills)

        self.attack_points *= 2


class ConsoleOutput:
    def __init__(self, general_settings):
        self.general_settings = general_settings

    def write_message(self, text):
        print(text)

    def write_message_with_delay_after(self, text, long_delay=False):
        self.write_message(text)

        if self.general_settings.get('UseDelay', True):
            time_to_sleep = random.randint(*self.general_settings['Delay'])
            if not long_delay:
                time_to_sleep /= 10
            sleep(time_to_sleep)


class Game:
    """Класс процесса игры."""

    def __init__(self, thing_settings, person_settings, general_settings,
                 things_pre_list, persons_pre_list, persons_skills):
        self.general_settings = general_settings
        self.thing_settings = thing_settings
        self.person_settings = person_settings

        self.things_pre_list = things_pre_list
        self.persons_skills = persons_skills
        self.persons_pre_list = persons_pre_list

        self.things = []
        self.warriors = []

    def __create_things(self):
        things = []

        things_pre_list_count = len(self.things_pre_list)
        max_gear_count = (self.general_settings['WarriorsCount'] *
                          self.general_settings['GearInOneHand'][1])

        while len(things) < max_gear_count:
            tid = random.randint(0, things_pre_list_count - 1)

            pre_name, is_weapon, is_clothes, variants = \
                self.things_pre_list[tid]
            name = pre_name + variants[random.randint(0, len(variants) - 1)]
            defence_percent = random.randint(
                *self.thing_settings['DefencePercent'])
            attack_points = random.randint(
                *self.thing_settings['AttackPoints'])
            health_points = random.randint(
                *self.thing_settings['HealthPoints'])

            things.append(
                Thing(
                    name=name,
                    defence_percent=defence_percent,
                    attack_points=attack_points,
                    health_points=health_points,
                    is_weapon=is_weapon,
                    is_clothes=is_clothes)
            )

        self.things = sorted(things, key=lambda v: v.defence_percent)

    def __create_warriors(self):
        warriors_variants = (Paladin.__name__, Warrior.__name__)

        persons_list = list(self.persons_pre_list)

        warriors_max_count = self.general_settings['WarriorsCount']
        persons_list_count = len(persons_list)
        if warriors_max_count > persons_list_count:
            warriors_max_count = persons_list_count

        # генерируем список скилов для не уникальных персонажей
        skills_not_unique = [skill for skill in self.persons_skills
                             if not skill.get('unique_skill', False)]

        while len(self.warriors) < warriors_max_count:
            persons_list_count = len(persons_list)
            pid = random.randint(0, persons_list_count - 1)

            name, is_unique = persons_list.pop(pid)
            defence_percent = random.randint(
                *self.person_settings['DefencePercent'])
            attack_points = random.randint(
                *self.person_settings['AttackPoints'])
            health_points = random.randint(
                *self.person_settings['HealthPoints'])
            warrior_class = random.choice(warriors_variants)

            skill_list = self.persons_skills if is_unique else \
                skills_not_unique

            constructor = globals()[warrior_class]
            self.warriors.append(
                constructor(name=name,
                            defence_percent=defence_percent,
                            attack_points=attack_points,
                            health_points=health_points,
                            is_unique=is_unique,
                            skills=skill_list)
            )

    def __gear_up_warriors(self):
        for person in self.warriors:
            gear_count = random.randint(
                *self.general_settings.get('GearInOneHand', (1, 1)))

            things = []
            for i in range(gear_count):
                things_count = len(self.things)
                thing = self.things.pop(random.randint(0, things_count - 1))

                things.append(thing)

            person.set_things(things)

    def __choose_skill(self, warrior, skill_list):
        for skill in getattr(warrior, skill_list):
            skill_applied = random.choices(
                [True, False],
                weights=[skill['probability'], 1 - skill['probability']])[0]
            if skill_applied or True:
                return skill

        return None

    def console_game_process(self):
        console = ConsoleOutput(self.general_settings)

        console.write_message_with_delay_after(
            'Отгружаем снаряжение со склада...', long_delay=True)
        self.__create_things()

        console.write_message_with_delay_after('Призываем воинов на арену...',
                                               long_delay=True)
        self.__create_warriors()

        console.write_message_with_delay_after('Раздаем снаряжение...',
                                               long_delay=True)
        self.__gear_up_warriors()

        console.write_message_with_delay_after('Да начнется битва!',
                                               long_delay=True)
        console.write_message('')

        arena_round = 0

        while len(self.warriors) > 1:
            arena_round += 1
            warriors = random.sample(self.warriors, 2)
            attack, defend = warriors

            # выяснеям количество поинтов атаки
            attack_damage = round(
                attack.total_attack_points() *
                (1 - defend.total_final_protection()))

            attack_hp = attack.total_health_points()
            defend_hp = defend.total_health_points()

            base_text = (f'>>> Раунд #{arena_round:003n}: 🗡 {attack.name}'
                         f'[{attack_hp}➕] '
                         f'наносит удар по 🛡 {defend.name}[{defend_hp}➕]')
            damage_text = f' и отнимает {attack_damage}hp'

            defend.decrease_health_points(attack_damage)

            text = base_text + damage_text
            console.write_message_with_delay_after(text, long_delay=False)

            dead_warrior = None
            for warrior in warriors:
                if warrior.total_health_points() == 0:
                    index = self.warriors.index(warrior)
                    dead_warrior = self.warriors.pop(index)

            if isinstance(dead_warrior, Person):
                console.write_message_with_delay_after(
                    f'💀 {dead_warrior.name} повержен!', long_delay=True)

        print(f'🏆 {self.warriors[0].name} вышел победителем из этой жестокой '
              f'битвы')
