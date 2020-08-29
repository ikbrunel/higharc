from django.db.models import Model, UUIDField, TextField
from uuid import uuid4

class Smoothie(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = TextField(unique=True, max_length=255, blank=False, null=True)
