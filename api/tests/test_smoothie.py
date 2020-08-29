from django.test import TestCase
from api.models import Smoothie


class SmoothieTests(TestCase):

    def test_smoothie_creation(self):
        """
        Ensure that we can create and save smoothies.
        """
        smoothie = Smoothie()
        smoothie.save()

        self.assertTrue(Smoothie.objects.filter(id=smoothie.id).exists())
