from django.test import TestCase

from common.tests.factories import BenevoleFactory
from permanence.models import PermanenceDay

# from permanence.tests.factories import PermanenceDayFactory


class myFirstTest(TestCase):
    def test_true_is_not_false(self):
        self.assertTrue(True)


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
