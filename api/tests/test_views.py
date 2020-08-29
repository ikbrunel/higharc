from api.models import Smoothie
from django.urls import reverse
from json import loads
from rest_framework.test import APITestCase
from uuid import uuid4


class ViewTests(APITestCase):

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
