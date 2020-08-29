from api.views import SmoothieViewSet
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register(r'smoothie', SmoothieViewSet, basename='smoothie')

urlpatterns = api_router.urls
