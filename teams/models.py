from django.db import models

# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=100)
    player_count = models.IntegerField()
    year_founded = models.IntegerField()
    owner_email = models.CharField(max_length=100)
