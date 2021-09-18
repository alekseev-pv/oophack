import unittest

from game import Person, Thing


class TestPerson(unittest.TestCase):
    def setUp(self):
        things = [
            Thing(name='Pistol', defence_percent=0, attack_points=50,
                  health_points=0),
            Thing(name='Helmet', defence_percent=10, attack_points=0,
                  health_points=20)
        ]

        self.person_with_things = Person(
            name='Person01', defence_percent=10, attack_points=20,
            health_points=100)
        self.person_without_things = Person(
            name='Person02', defence_percent=35, attack_points=10,
            health_points=100)

        self.person_with_things.set_things(things)

    def test_persons_health_points_with_things(self):
        call = self.person_with_things.total_health_points()
        result = 120
        self.assertEqual(call, result)

    def test_persons_defence_percent_with_things(self):
        call = self.person_with_things.total_defence_percent()
        result = 20
        self.assertEqual(call, result)

    def test_persons_final_protection_with_things(self):
        call = self.person_with_things.total_final_protection()
        result = 0.2
        self.assertEqual(call, result)

    def test_persons_attack_points_with_things(self):
        call = self.person_with_things.total_attack_points()
        result = 70
        self.assertEqual(call, result)

    def test_persons_health_points_without_things(self):
        call = self.person_without_things.total_health_points()
        result = 100
        self.assertEqual(call, result)

    def test_persons_defence_percent_without_things(self):
        call = self.person_without_things.total_defence_percent()
        result = 35
        self.assertEqual(call, result)

    def test_persons_final_protection_without_things(self):
        call = self.person_without_things.total_final_protection()
        result = 0.35
        self.assertEqual(call, result)

    def test_persons_attack_points_without_things(self):
        call = self.person_without_things.total_attack_points()
        result = 10
        self.assertEqual(call, result)
