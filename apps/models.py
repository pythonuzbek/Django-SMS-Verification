from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, PositiveBigIntegerField, UUIDField
import uuid

# Create your models here.


class User(AbstractUser):
    id = UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    phone = CharField(max_length=15)
    confirm = PositiveBigIntegerField(null=True, blank=True)

