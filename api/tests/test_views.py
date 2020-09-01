from api.models import Smoothie, SmoothieIngredient
from django.urls import reverse
from json import loads
from random import randint
from rest_framework.test import APITestCase
from .smoothie_tests import SmoothieTests
from uuid import uuid4
from urllib.parse import urlencode


class SmoothieViewTests(SmoothieTests):

    def test_get_smoothie_with_no_smoothies(self):
        """
        If we have no smoothies, we should return an empty list.
        """
        url = reverse('smoothie-list')
        user_id = self.gensym()
        url = url + '?' + urlencode({'user_id': user_id})
        response = self.client.get(url)  # heinous, DRF seems to be ignoring data -> query params pipeline

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(loads(response.content)))

    def test_must_request_smoothie_with_user_id(self):
        url = reverse('smoothie-list')
        response = self.client.get(url)

        self.assertEqual(400, response.status_code)

    def test_cant_get_someone_elses_smoothie(self):
        url = reverse('smoothie-list')
        user_id = self.gensym()
        Smoothie.objects.create(
            name=self.gensym(), user_id=user_id)
        url = url + '?' + urlencode({'user_id': uuid4()})
        response = self.client.get(url)  # heinous, DRF seems to be ignoring data -> query params pipeline

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(loads(response.content)))

    def test_can_get_ones_own_smoothie(self):
        url = reverse('smoothie-list')
        user_id = self.gensym()
        Smoothie.objects.create(
            name=self.gensym(), user_id=user_id)
        url = url + '?' + urlencode({'user_id': user_id})
        response = self.client.get(url)  # heinous, DRF seems to be ignoring data -> query params pipeline

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(loads(response.content)))

    def test_get_smoothie_with_one_smoothie(self):
        """
        If we have 1 smoothie, we get a list of length 1 and the smoothie.
        """
        url = reverse('smoothie-list')
        smoothie = Smoothie.objects.create(
            name=str(uuid4()), user_id=self.gensym())

        response = loads(self.client.get(
            url + '?' + urlencode({'user_id': smoothie.user_id})
        ).content)
        found_smoothie = response[0]

        self.assertEqual(1, len(response))
        self.assertEqual(str(smoothie.id), found_smoothie['id'])
        self.assertEqual(smoothie.name, found_smoothie['name'])

    def test_create_a_new_smoothie_via_api(self):
        url = reverse('smoothie-list')
        smoothie_name = self.gensym()
        user_id = self.gensym()
        data = {
            'name': smoothie_name,
            'user_id': user_id
        }

        raw_response = self.client.post(
            url,
            data,
            format='json')
        response = loads(raw_response.content)

        self.assertEqual(201, raw_response.status_code)

        found_smoothie = Smoothie.objects.get(id=response['id'])

        self.assertEqual(
            smoothie_name,
            found_smoothie.name)
        self.assertEqual(
            user_id,
            str(found_smoothie.user_id))

    def test_unique_smoothie_names(self):
        url = reverse('smoothie-list')
        smoothie = Smoothie.objects.create(
            name=self.gensym(), user_id=self.gensym())
        data = {
            'name': smoothie.name,
            'user_id': smoothie.user_id
        }

        response = self.client.post(
            url, data, format='json')

        self.assertEquals(400, response.status_code)
        self.assertEquals(
            {'name': ['smoothie with this name already exists.']},
            loads(response.content))

    def test_update_smoothie_name(self):
        url = reverse('smoothie-list')
        user_id = self.gensym()

        smoothie_name = self.gensym()
        smoothie_updated_name = self.gensym()

        smoothie = Smoothie.objects.create(
            name=smoothie_name,
            user_id=user_id)
        data = {
            'id': smoothie.id,
            'name': smoothie_updated_name,
            'user_id': user_id
        }

        response = self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json')

        self.assertEquals(200, response.status_code)

        smoothie.refresh_from_db()

        self.assertEquals(
            smoothie_updated_name,
            smoothie.name)

    def test_cant_update_someone_elses_smoothie(self):
        url = reverse('smoothie-list')
        user_id = self.gensym()

        smoothie_name = self.gensym()
        smoothie_updated_name = self.gensym()

        smoothie = Smoothie.objects.create(
            name=smoothie_name,
            user_id=user_id)
        data = {
            'id': smoothie.id,
            'name': smoothie_updated_name,
            'user_id': self.gensym()
        }

        response = self.client.patch(
            url + str(smoothie.id) + '/',
            data,
            format='json')

        self.assertEquals(404, response.status_code)

        smoothie.refresh_from_db()

        self.assertEquals(
            smoothie_name,
            smoothie.name)


class SmoothieIngredientTests(SmoothieTests):

    def test_can_create_ingredients(self):
        url = reverse('smoothie-ingredient-list')
        user_id = self.gensym()
        smoothie = Smoothie.objects.create(
            name=self.gensym, user_id=user_id)
        ingredient_name = self.gensym()
        ingredient_quantity = randint(0, 10)

        data = {
            'name': ingredient_name,
            'quantity': ingredient_quantity,
            'smoothie': smoothie.id,
            'user_id': user_id
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

    def test_cant_associate_ingredients_with_other_folks_smoothies(self):
        url = reverse('smoothie-ingredient-list')
        user_id = self.gensym()
        smoothie = Smoothie.objects.create(
            name=self.gensym, user_id=user_id)
        ingredient_name = self.gensym()
        ingredient_quantity = randint(0, 10)

        data = {
            'name': ingredient_name,
            'quantity': ingredient_quantity,
            'smoothie': smoothie.id,
            'user_id': self.gensym()
        }

        raw_response = self.client.post(
            url,
            data,
            format='json'
        )
        self.assertEquals(400, raw_response.status_code)
        msg = 'You may not add ingredients to someone else''s smoothie.'
        self.assertEquals(
            {'smoothie': [msg], 'user_id': [msg]},
            loads(raw_response.content))
