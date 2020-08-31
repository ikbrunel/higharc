from api.models import Smoothie, SmoothieIngredient
from rest_framework.serializers import (
    ModelSerializer, ValidationError, UUIDField)
from rest_framework.viewsets import ModelViewSet


# TODO: factor into api/serializers/smoothie_ingredient_serializer
class SmoothieIngredientSerializer(ModelSerializer):
    id = UUIDField(required=False)

    class Meta:
        model = SmoothieIngredient
        fields = ['id', 'name', 'quantity']


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

    def update(self, instance, validated_data):
        ingredients_existing = instance.ingredients.all()
        ingredients_raw = validated_data.pop('ingredients')
        instance_qs = Smoothie.objects.filter(id=instance.id)
        instance_qs.update(**validated_data)
        for ingredient_raw in ingredients_raw:
            if 'id' in ingredient_raw:
                ingredient_id = ingredient_raw.pop('id')
                if not ingredients_existing.filter(id=ingredient_id).exists():
                    # Edits on not-this-smoothie's ingredients are disallowed
                    raise ValidationError(
                        {'ingredients':

                         'Ingredient %s not associated with smoothie %s' %
                         (ingredient_id, instance.id)})
                else:
                    ingredients_existing.filter(
                        id=ingredient_id).update(**ingredient_raw)
        return instance


class SmoothieViewSet(ModelViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
