from api.models import Smoothie, SmoothieIngredient
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField


class SmoothieSerializer(ModelSerializer):
    ingredients = HyperlinkedRelatedField(
        many=True, required=False, view_name='smoothie-ingredient-detail',
        queryset=SmoothieIngredient.objects.all())

    class Meta:
        model = Smoothie
        fields = ['id', 'name', 'ingredients']
