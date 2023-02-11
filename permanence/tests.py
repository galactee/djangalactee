from django.test import TestCase


class myFirstTest(TestCase):
    def test_true_is_not_false(self):
        self.assertTrue(True)
