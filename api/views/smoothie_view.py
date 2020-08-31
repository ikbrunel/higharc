from api.models import Smoothie, SmoothieIngredient
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


# TODO: factor into api/serializers/smoothie_ingredient_serializer
class SmoothieIngredientSerializer(ModelSerializer):
    class Meta:
        model = SmoothieIngredient
        fields = ['name', 'quantity']


# TODO: factor into api/serializers/smoothie_serializer
class SmoothieSerializer(ModelSerializer):
    ingredients = SmoothieIngredientSerializer(
        many=True)

    class Meta:
        model = Smoothie
        fields = ['id', 'name', 'ingredients']

    def is_valid(self, *args, **kwargs):
        super(SmoothieSerializer, self).is_valid(*args, **kwargs)

    def create(self, validated_data):
        ingredients_raw = validated_data.pop('ingredients')
        smoothie = Smoothie.objects.create(**validated_data)
        for ingredient_raw in ingredients_raw:
            SmoothieIngredient.objects.create(
                smoothie=smoothie,
                **ingredient_raw)
        return smoothie



class SmoothieViewSet(ModelViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
