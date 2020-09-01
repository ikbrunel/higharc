from rest_framework.test import APITestCase
from uuid import uuid4


class SmoothieTests(APITestCase):

    @staticmethod
    def gensym():
        return str(uuid4())
