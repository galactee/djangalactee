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

    def test_get_inscriptions_for_february_2023(self):
        def construct_data():
            # three inscriptions in february, will be in result
            PermanenceDayFactory(
                date="2023-02-09",
                inscrite_1=self.benevole_marie,
                inscrite_3=self.benevole_olivia,
            )
            PermanenceDayFactory(
                date="2023-02-01",
                inscrite_2=self.benevole_marie,
                inscrite_4=self.benevole_noelle,
            )
            PermanenceDayFactory(
                date="2023-02-28",
                inscrite_2=self.benevole_marie,
                inscrite_3=self.benevole_olivia,
                inscrite_4=self.benevole_noelle,
            )
            # one inscription in march, should not be in result
            PermanenceDayFactory(
                date="2023-03-28",
                inscrite_2=self.benevole_marie,
                inscrite_3=self.benevole_olivia,
                inscrite_4=self.benevole_noelle,
            )

        construct_data()

        self.assertEqual(PermanenceDay.objects.count(), 4)
        self.assertEqual(PermanenceDay.objects.for_given_month(2023, 2).count(), 3)

    def test_next_inscriptions_for_benevole(self):
        pass
