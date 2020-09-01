from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from uuid import UUID


class UserIdFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.data.get('user_id')
        if not user_id:
            # for some reason DRF refuses to handle query params correctly in tests
            user_id = request.query_params.get('user_id')

        if not user_id:
            raise ValidationError(
                'Please provide a user_id parameter when querying this API.'
            )

        try:
            user_id = UUID(user_id)
        except ValueError:
            raise ValidationError(
                'Please submit a UUID as your user_id parameter.'
            )

        return queryset.filter(user_id=user_id)
