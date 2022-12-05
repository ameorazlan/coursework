from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


#Team model
class team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    player_count = models.IntegerField(validators = [MinValueValidator(11)])
    year_founded = models.IntegerField(validators = [MaxValueValidator(2022)])
    owner_email = models.EmailField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

#Fixture model which is to be plated with 2 teams
class fixtures(models.Model):
    #Makes sure that only 1 pair of team1 and team2 can exist
    class Meta:
        unique_together = ['team1', 'team2']
    team1 = models.ForeignKey(team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(team, on_delete=models.CASCADE, related_name='team2')
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

#Table model which is composed of many teams
class table(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    GP = models.IntegerField(default=0)
    GF = models.IntegerField(default=0)
    GA = models.IntegerField(default=0)

