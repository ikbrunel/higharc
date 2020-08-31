from api.models import Smoothie, SmoothieIngredient
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class SmoothieIngredientSerializer(ModelSerializer):
    class Meta:
        model = SmoothieIngredient
        fields = ['name', 'quantity']


class SmoothieSerializer(ModelSerializer):
    class Meta:
        model = Smoothie
        fields = ['id', 'name']


class SmoothieViewSet(ModelViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
