from api.models import Smoothie, SmoothieIngredient
from django.urls import reverse
from json import loads
from random import randint
from rest_framework.test import APITestCase
from uuid import uuid4


class SmoothieTests(APITestCase):

    @staticmethod
    def gensym():
        return str(uuid4())


class SmoothieViewTests(SmoothieTests):

    def test_get_smoothie_with_no_smoothies(self):
        """
        If we have no smoothies, we should return an empty list.
        """
        url = reverse('smoothie-list')
        response = loads(self.client.get(url).content)

        self.assertEqual(0, len(response))

    def test_get_smoothie_with_one_smoothie(self):
        """
        If we have 1 smoothie, we get a list of length 1 and the smoothie.
        """
        url = reverse('smoothie-list')
        smoothie = Smoothie.objects.create(name=str(uuid4()))

        response = loads(self.client.get(url).content)
        found_smoothie = response[0]

        self.assertEqual(1, len(response))
        self.assertEqual(str(smoothie.id), found_smoothie['id'])
        self.assertEqual(smoothie.name, found_smoothie['name'])

    def test_create_a_new_smoothie_via_api(self):
        url = reverse('smoothie-list')
        smoothie_name = str(uuid4())
        data = {
            'name': smoothie_name,
        }

        response = loads(self.client.post(
            url,
            data,
            format='json').content)

        found_smoothie = Smoothie.objects.get(id=response['id'])

        self.assertEqual(
            smoothie_name,
            found_smoothie.name)

    def test_update_smoothie_name(self):
        url = reverse('smoothie-list')

        smoothie_name = self.gensym()
        smoothie_updated_name = self.gensym()

        smoothie = Smoothie.objects.create(name=smoothie_name)
        data = {
            'id': smoothie.id,
            'name': smoothie_updated_name,
        }

        self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json').content

        smoothie.refresh_from_db()

        self.assertEquals(
            smoothie_updated_name,
            smoothie.name)


class SmoothieIngredientTests(SmoothieTests):

    def test_can_create_ingredients(self):
        url = reverse('smoothie-ingredient-list')
        smoothie = Smoothie.objects.create(name=self.gensym)
        ingredient_name = self.gensym()
        ingredient_quantity = randint(0, 10)

        data = {
            'name': ingredient_name,
            'quantity': ingredient_quantity,
            'smoothie': smoothie.id
        }

        response = loads(self.client.post(
            url,
            data,
            format='json'
        ).content)

        smoothie_ingredient = SmoothieIngredient.objects.get(
            id=response['id'])

        self.assertEquals(
            ingredient_name,
            smoothie_ingredient.name)
        self.assertEquals(
            ingredient_quantity,
            smoothie_ingredient.quantity)
