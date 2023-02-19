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
        permanence = PermanenceDay(
            date="2023-02-19",
            inscrite_1=BenevoleFactory(),
            inscrite_3=BenevoleFactory(),
        )
        permanence.save()
        self.assertEqual(PermanenceDay.objects.count(), 1)
        self.assertIsNone(permanence.inscrite_2)
