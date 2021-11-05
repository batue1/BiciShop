from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Los siguientes son los tipos de usuario logueados
class User(AbstractUser):
    es_vendedor  = models.BooleanField(default=False)
    es_comprador = models.BooleanField(default=True)

    class Meta:
        db_table = "auth_user"
