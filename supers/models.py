from django.db import models

# Create your models here.
from super_types.models import Super_types


class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    second_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type_id = models.ForeignKey(Super_types, on_delete=models.CASCADE)