from django.test import TestCase

from common.tests.factories import BenevoleFactory
from permanence.models import PermanenceDay
from permanence.tests.factories import PermanenceDayFactory


class PermanenceDayTest(TestCase):
    def test_object_creation(self):
        permanence = PermanenceDay(date="2023-02-19")
        permanence.save()
        self.assertEqual(PermanenceDay.objects.count(), 1)

    def test_no_display_empty_spots(self):
        first = BenevoleFactory()
        third = BenevoleFactory()
        permanence = PermanenceDay(
            date="2023-02-19",
            inscrite_1=first,
            inscrite_3=third,
        )
        permanence.save()
        self.assertEqual(PermanenceDay.objects.count(), 1)
        self.assertEqual(permanence.inscrite_1, first)
        self.assertIsNone(permanence.inscrite_2)
        self.assertEqual(permanence.inscrite_3, third)
        inscrites = permanence.inscrites
        self.assertEqual(len(inscrites), 2)
        self.assertEqual(inscrites[0], first)
        self.assertEqual(inscrites[1], third)


class PermanenceCountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.benevole_marie = BenevoleFactory(first_name="Marie", last_name="Covert")
        cls.benevole_noelle = BenevoleFactory(first_name="Noëlle", last_name="Mer")
        cls.benevole_olivia = BenevoleFactory(first_name="Olivia", last_name="Roly")
        cls.benevole_philomene = BenevoleFactory(
            first_name="Philomène", last_name="Aqua"
        )

        PermanenceDayFactory(
            date="2023-02-09",
            inscrite_1=cls.benevole_marie,
            inscrite_3=cls.benevole_olivia,
        )
        PermanenceDayFactory(
            date="2023-02-01",
            inscrite_2=cls.benevole_marie,
        )
        PermanenceDayFactory(
            date="2023-02-28",
            inscrite_2=cls.benevole_olivia,
            inscrite_3=cls.benevole_marie,
            inscrite_4=cls.benevole_noelle,
        )
        PermanenceDayFactory(
            date="2023-03-28",
            inscrite_3=cls.benevole_olivia,
            inscrite_4=cls.benevole_marie,
        )

    def test_get_inscriptions_for_february_2023(self):
        self.assertEqual(PermanenceDay.objects.count(), 4)
        self.assertEqual(PermanenceDay.objects.for_given_month(2023, 2).count(), 3)

    def test_inscriptions_for_benevole(self):
        self.assertEqual(
            4, PermanenceDay.objects.for_benevole(self.benevole_marie).count()
        )
        self.assertEqual(
            3, PermanenceDay.objects.for_benevole(self.benevole_olivia).count()
        )
        self.assertEqual(
            1, PermanenceDay.objects.for_benevole(self.benevole_noelle).count()
        )
        self.assertEqual(
            0, PermanenceDay.objects.for_benevole(self.benevole_philomene).count()
        )
