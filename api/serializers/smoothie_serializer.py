from api.models import Smoothie, SmoothieIngredient
from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField, UUIDField)


class SmoothieSerializer(ModelSerializer):
    ingredients = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Smoothie
        fields = ['id', 'name', 'ingredients']
