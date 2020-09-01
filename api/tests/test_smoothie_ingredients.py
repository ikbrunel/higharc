from api.models import Smoothie, SmoothieIngredient
from django.test import TestCase
from .smoothie_tests import SmoothieTests
from uuid import uuid4


class SmoothieIngredientTests(SmoothieTests):

    def test_can_add_ingredients_to_a_smoothie(self):
        smoothie = Smoothie.objects.create(
            name=self.gensym(), user_id=self.gensym())
        ingredient_1 = SmoothieIngredient(
            name=self.gensym(),
            quantity=1,
            smoothie=smoothie,
            user_id=smoothie.user_id)
        ingredient_1.save()

        found_smoothie = Smoothie.objects.get(id=smoothie.id)
        found_ingredients = found_smoothie.ingredients.all()
        self.assertEqual(
            found_ingredients.count(),
            1)
        self.assertEqual(ingredient_1.name, found_ingredients[0].name)
        self.assertEqual(ingredient_1.quantity, found_ingredients[0].quantity)
