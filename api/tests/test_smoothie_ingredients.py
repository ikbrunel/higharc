from api.models import Smoothie, SmoothieIngredient
from django.test import TestCase
from uuid import uuid4


class SmoothieIngredientTests(TestCase):

    def test_can_add_ingredients_to_a_smoothie(self):
        smoothie = Smoothie(name=str(uuid4()))
        smoothie.save()
        ingredient_1 = SmoothieIngredient(
            name=str(uuid4()),
            quantity=1)
        ingredient_1.save()
        ingredient_1.smoothies.add(smoothie)

        found_smoothie = Smoothie.objects.get(id=smoothie.id)
        found_ingredients = found_smoothie.smoothieingredient_set.all()
        self.assertEqual(
            found_ingredients.count(),
            1)
        self.assertEqual(ingredient_1.name, found_ingredients[0].name)
        self.assertEqual(ingredient_1.quantity, found_ingredients[0].quantity)
