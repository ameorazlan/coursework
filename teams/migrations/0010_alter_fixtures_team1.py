# Generated by Django 4.1.1 on 2022-12-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_team_image_alter_team_owner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='teams.team', unique=True),
        ),
    ]
