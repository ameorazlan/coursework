from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    player_count = models.IntegerField(validators = [MinValueValidator(11)])
    year_founded = models.IntegerField(validators = [MaxValueValidator(2022)])
    owner_email = models.CharField(max_length=100)


