from api.models import SmoothieIngredient
from api.serializers import SmoothieIngredientSerializer
from rest_framework.viewsets import ModelViewSet


class SmoothieIngredientViewSet(ModelViewSet):
    queryset = SmoothieIngredient.objects.all()
    serializer_class = SmoothieIngredientSerializer
