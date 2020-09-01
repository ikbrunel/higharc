from api.models import Smoothie
from django.db.utils import IntegrityError
from .smoothie_tests import SmoothieTests


class SmoothieTests(SmoothieTests):

    def test_smoothie_creation(self):
        """
        Ensure that we can create and save smoothies.
        """
        smoothie = Smoothie(name=self.gensym(), user_id=self.gensym())
        smoothie.save()

        self.assertTrue(Smoothie.objects.filter(id=smoothie.id).exists())

    def test_unique_names(self):
        smoothie = Smoothie.objects.create(
            name=self.gensym(), user_id=self.gensym())
        with self.assertRaises(IntegrityError):
            Smoothie.objects.create(
                name=smoothie.name)
