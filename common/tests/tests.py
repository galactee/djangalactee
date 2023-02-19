from django.test import TestCase

from .factories import BenevoleFactory


class TestBenevoleFactory(TestCase):
    def test_i_can_generate_several_benevoles(self):
        benevole_1 = BenevoleFactory()
        benevole_2 = BenevoleFactory()
        self.assertNotEqual(benevole_1.email, benevole_2.email)
        self.assertNotEqual(benevole_1.username, benevole_2.username)
