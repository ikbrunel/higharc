from api.models import Smoothie
from api.serializers import SmoothieSerializer
from rest_framework.viewsets import ModelViewSet


class SmoothieViewSet(ModelViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
