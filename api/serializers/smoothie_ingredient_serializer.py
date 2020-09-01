from api.models import SmoothieIngredient
from rest_framework.serializers import ModelSerializer, UUIDField


class SmoothieIngredientSerializer(ModelSerializer):
    id = UUIDField(required=False)

    class Meta:
        model = SmoothieIngredient
        fields = ['id', 'name', 'quantity', 'smoothie']
