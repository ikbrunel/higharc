from api.models import SmoothieIngredient
from api.serializers import SmoothieIngredientSerializer
from .user_id_viewset import UserIdViewSet


class SmoothieIngredientViewSet(UserIdViewSet):
    queryset = SmoothieIngredient.objects.all()
    serializer_class = SmoothieIngredientSerializer
