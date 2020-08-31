from api.models import Smoothie
from django.urls import reverse
from json import dumps, loads
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

    def test_create_a_new_smoothie(self):
        url = reverse('smoothie-list')
        smoothie_name = uuid4()

        response = loads(self.client.post(
            url,
            data={'name': smoothie_name},
            HTTP_ACCEPT='application/json').content)

        found_smoothie = Smoothie.objects.get(id=response['id'])
        self.assertEqual(
            str(smoothie_name),
            found_smoothie.name)
