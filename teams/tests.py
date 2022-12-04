from django.test import TestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction
from .models import team, fixtures, table
from django.urls import reverse
from .forms import fixtureForm
# Create your tests here.
class TeamsTests(TestCase):
    @classmethod
    def setUp(cls):
        t1 = team(name = 'Test Team', player_count = 13, year_founded = 2022, owner_email='test_team@gmail.com')
        t1.save()
        t2 = team(name = 'Test Team2', player_count = 13, year_founded = 2022, owner_email='test_team2@gmail.com')
        t2.save()
    def test_save_team(self):
        db_count = team.objects.all().count()
        t3 = team(name = 'Test Team3', player_count = 13, year_founded = 2022, owner_email='test_team3@gmail.com')
        t3.save()
        self.assertEqual(db_count+1, team.objects.all().count())
    def test_duplicate_title(self):
        db_count = team.objects.all().count()
        t = team(name = 'Test Team', player_count = 13, year_founded = 2022, owner_email='test_team3@gmail.com')
        try:
            with transaction.atomic():
                t.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, team.objects.all().count())

class FixturesTest(TestCase):
    @classmethod
    def setUp(cls):
        t1 = team(name = 'Test Team', player_count = 13, year_founded = 2022, owner_email='test_team@gmail.com')
        t1.save()
        t2 = team(name = 'Test Team2', player_count = 13, year_founded = 2022, owner_email='test_team2@gmail.com')
        t2.save()
        f1 = fixtures(team1 = t1, team2 = t2, score1 = 2, score2 = 3)
        f1.save()
        f2 = fixtures(team1 = t2, team2 = t1, score1 = 0, score2 = 2)
        f2.save()
    def test_save_team(self):
        db_count = team.objects.all().count()
        t3 = team(name = 'Test Team3', player_count = 13, year_founded = 2022, owner_email='test_team3@gmail.com')
        t3.save()
        t4 = team(name = 'Test Team4', player_count = 13, year_founded = 2022, owner_email='test_team4@gmail.com')
        t4.save()
        f3 = fixtures(team1 = t4, team2 = t3, score1 = 0, score2 = 2)
        f3.save()
        self.assertEqual(db_count+1, fixtures.objects.all().count())
    def test_duplicate_title(self):
        t4 = team(name = 'Test Team4', player_count = 13, year_founded = 2022, owner_email='test_team4@gmail.com')
        t4.save()
        t5 = team(name = 'Test Team5', player_count = 13, year_founded = 2022, owner_email='test_team5@gmail.com')
        t5.save()
        f = fixtures(team1 = t4, team2 = t5, score1 = 0, score2 = 1)
        f.save()
        db_count = fixtures.objects.all().count()
        f2 = fixtures(team1 = t4, team2 = t5, score1 = 0, score2 = 1)
        try:
            with transaction.atomic():
                f2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, fixtures.objects.all().count())
