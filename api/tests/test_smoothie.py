from api.models import Smoothie
from django.db.utils import IntegrityError
from django.test import TestCase
from uuid import uuid4


class SmoothieTests(TestCase):

    def test_smoothie_creation(self):
        """
        Ensure that we can create and save smoothies.
        """
        smoothie = Smoothie()
        smoothie.save()

        self.assertTrue(Smoothie.objects.filter(id=smoothie.id).exists())

    def test_unique_names(self):
        smoothie = Smoothie.objects.create(
            name=str(uuid4()))
        with self.assertRaises(IntegrityError):
            Smoothie.objects.create(
                name=smoothie.name)
