from django.db.models import (
    Model, UUIDField, IntegerField, TextField, ManyToManyField)
from uuid import uuid4

from .smoothie import Smoothie


class SmoothieIngredient(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    # TODO: refactor this onerous PK into a reusable field, since we're going
    # to use it everywhere.
    smoothies = ManyToManyField(Smoothie, related_name='ingredients')
    name = TextField(max_length=255, blank=False, null=False)
    quantity = IntegerField()
