# Generated by Django 4.1.1 on 2022-12-02 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_rename_teams_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='player_count',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='size',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
