from api.models import Smoothie
from api.serializers import SmoothieSerializer
from .user_id_viewset import UserIdViewSet


class SmoothieViewSet(UserIdViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
