from api.models import Smoothie, SmoothieIngredient
from api.views.smoothie_view import SmoothieSerializer  # stinky import
from django.test import TestCase
from random import randint
from rest_framework.serializers import ValidationError
from uuid import uuid4


class SerializerTests(TestCase):

    @staticmethod
    def gensym():
        return str(uuid4())

    def test_nested_creation(self):
        smoothie_name = self.gensym()
        ingredient_name = self.gensym()
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

    def test_update_smoothie_name(self):
        smoothie_name = self.gensym()
        smoothie_updated_name = self.gensym()
        ingredient_name = self.gensym()
        ingredient_quantity = 1

        smoothie = Smoothie.objects.create(name=smoothie_name)
        ingredient = SmoothieIngredient.objects.create(
            name=ingredient_name, quantity=ingredient_quantity,
            smoothie=smoothie)

        data_update = {
            'id': smoothie.id,
            'name': smoothie_updated_name,
            'ingredients': [{
                'id': ingredient.id,
                'name': ingredient_name,
                'quantity': ingredient_quantity
            }]
        }
        serializer = SmoothieSerializer(instance=smoothie, data=data_update)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        smoothie.refresh_from_db()

        self.assertEquals(
            smoothie_updated_name,
            smoothie.name)
