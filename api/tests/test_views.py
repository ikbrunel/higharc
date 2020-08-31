from api.models import Smoothie, SmoothieIngredient
from django.urls import reverse
from json import dumps, loads
from random import randint
from rest_framework.test import APITestCase
from uuid import uuid4


class ViewTests(APITestCase):

    @staticmethod
    def gensym():
        return str(uuid4())

    def test_get_smoothie_with_no_smoothies(self):
        """
        If we have no smoothies, we should return an empty list.
        """
        url = reverse('smoothie-list')
        response = loads(self.client.get(url).content)

        self.assertEqual(0, len(response))

    def test_get_smoothie_with_one_smoothies(self):
        """
        If we have 1 smoothie, we get a list of length 1 and the smoothie.
        """
        url = reverse('smoothie-list')
        smoothie = Smoothie(name=str(uuid4()))
        smoothie.save()
        response = loads(self.client.get(url).content)
        found_smoothie = response[0]

        self.assertEqual(1, len(response))
        self.assertEqual(str(smoothie.id), found_smoothie['id'])
        self.assertEqual(smoothie.name, found_smoothie['name'])

    def test_create_a_new_smoothie(self):
        url = reverse('smoothie-list')
        smoothie_name = str(uuid4())
        ingredient_name = str(uuid4())
        ingredient_count = randint(0, 10)
        data = {
                'name': smoothie_name,
                'ingredients': [
                    {
                        'name': ingredient_name,
                        'quantity': ingredient_count
                     },
                ]
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
        ingredient_name = self.gensym()
        ingredient_quantity = 1

        smoothie = Smoothie.objects.create(name=smoothie_name)
        ingredient = SmoothieIngredient.objects.create(
            name=ingredient_name, quantity=ingredient_quantity,
            smoothie=smoothie)

        data = {
            'id': smoothie.id,
            'name': smoothie_updated_name,
            'ingredients': [{
                'id': ingredient.id,
                'name': ingredient_name,
                'quantity': ingredient_quantity
            }]
        }

        self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json').content

        smoothie.refresh_from_db()

        self.assertEquals(
            smoothie_updated_name,
            smoothie.name)

    def test_cant_update_ingredients_not_on_specified_smoothie(self):
        url = reverse('smoothie-list')

        smoothie_name = self.gensym()
        ingredient_name = self.gensym()
        ingredient_updated_name = self.gensym()
        ingredient_quantity = 1

        smoothie = Smoothie.objects.create(name=smoothie_name)
        ingredient = SmoothieIngredient.objects.create(
            name=ingredient_name, quantity=ingredient_quantity,
            smoothie=smoothie)

        another_smoothie = Smoothie.objects.create(name=self.gensym())
        another_ingredient = SmoothieIngredient.objects.create(
            name=self.gensym(), quantity=ingredient_quantity,
            smoothie=another_smoothie)

        data = {
            'id': smoothie.id,
            'name': smoothie_name,
            'ingredients': [{
                'id': another_ingredient.id,
                'name': ingredient_updated_name,
                'quantity': ingredient_quantity
            }]
        }

        response = self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json')

        self.assertEqual(400, response.status_code)

        ingredient.refresh_from_db()

        self.assertEquals(
            ingredient_name,
            ingredient.name)

    def test_can_update_ingredients(self):
        url = reverse('smoothie-list')

        smoothie_name = self.gensym()
        ingredient_name = self.gensym()
        ingredient_updated_name = self.gensym()
        ingredient_quantity = 1
        ingredient_updated_quantity = 6

        smoothie = Smoothie.objects.create(name=smoothie_name)
        ingredient = SmoothieIngredient.objects.create(
            name=ingredient_name, quantity=ingredient_quantity,
            smoothie=smoothie)

        data = {
            'id': smoothie.id,
            'name': smoothie_name,
            'ingredients': [{
                'id': ingredient.id,
                'name': ingredient_updated_name,
                'quantity': ingredient_updated_quantity
            }]
        }

        self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json')

        ingredient.refresh_from_db()

        self.assertEquals(
            ingredient_updated_name,
            ingredient.name)
        self.assertEquals(
            ingredient_updated_quantity,
            ingredient.quantity)
