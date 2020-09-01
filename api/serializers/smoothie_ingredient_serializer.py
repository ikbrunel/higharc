from api.models import Smoothie, SmoothieIngredient
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, UUIDField


class SmoothieIngredientSerializer(ModelSerializer):
    id = UUIDField(required=False)
    MULTITENANT_ERROR_MESSAGE = \
        'You may not add ingredients to someone else''s smoothie.'

    def validate(self, data):
        smoothie = data.get('smoothie')
        user_id = data.get('user_id')

        if smoothie.user_id != user_id:
            raise ValidationError(
                {'user_id': self.MULTITENANT_ERROR_MESSAGE,
                 'smoothie': self.MULTITENANT_ERROR_MESSAGE}
                )
        return data

    class Meta:
        model = SmoothieIngredient
        fields = ['id', 'name', 'quantity', 'smoothie', 'user_id']
