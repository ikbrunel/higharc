from api.views import SmoothieViewSet, SmoothieIngredientViewSet
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register(
    r'smoothie', SmoothieViewSet, basename='smoothie')
api_router.register(
    r'ingredient', SmoothieIngredientViewSet, basename='smoothie-ingredient')

urlpatterns = api_router.urls
