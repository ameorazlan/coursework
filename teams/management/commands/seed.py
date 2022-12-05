from django.core.management.base import BaseCommand
from teams.models import *

#Seeds database with some team and fixtures objects
#Note that only 2 sample universities will be seeded here, the rest were inputted manually in the forms
class Command(BaseCommand):
    def handle(self, *args, **options):
        t1 = team.objects.get(id=37)
        t2 = team.objects.get(id=38)
        t1.delete()
        t2.delete()