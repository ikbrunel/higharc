from rest_framework.viewsets import ModelViewSet
from api.filters import UserIdFilter


class UserIdViewSet(ModelViewSet):
    filter_backends = [UserIdFilter]
    search_fields = 'user_id'
