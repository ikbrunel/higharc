from api.models import Smoothie
from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField,
)


class SmoothieSerializer(ModelSerializer):
    ingredients = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Smoothie
        fields = ['id', 'name', 'ingredients', 'user_id']
