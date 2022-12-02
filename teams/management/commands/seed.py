from django.core.management.base import BaseCommand
from teams.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        team.objects.all().delete()
        t=team(name="Manchester City", player_count=20, year_founded=1880, owner_email="mancity@gmail.com")
        t.save()
        self.stdout.write('done.') 