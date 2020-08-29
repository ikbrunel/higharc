from api.models import Smoothie
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class SmoothieSerializer(ModelSerializer):
    class Meta:
        model = Smoothie
        fields = ['id', 'name']


class SmoothieViewSet(ModelViewSet):
    queryset = Smoothie.objects.all()
    serializer_class = SmoothieSerializer
