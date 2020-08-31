from api.views.smoothie_view import SmoothieSerializer  # stinky import
from django.test import TestCase
from random import randint
from uuid import uuid4


class SerializerTests(TestCase):

    def test_nested_creation(self):
        smoothie_name = str(uuid4())
        ingredient_name = str(uuid4())
        ingredient_count = randint(0, 10)
        data = {
            'name': smoothie_name,
            'ingredients': [
                {
                    'name': ingredient_name,
                    'quantity': ingredient_count
                 }
            ]
        }
        serializer = SmoothieSerializer(
            data=data
        )
        serializer.is_valid(raise_exception=True)

        created_smoothie = serializer.save()

        self.assertEqual(
            smoothie_name, created_smoothie.name)
        self.assertEqual(
            1,
            created_smoothie.ingredients.all().count())
        self.assertEqual(
            ingredient_count,
            created_smoothie.ingredients.all()[0].quantity)
