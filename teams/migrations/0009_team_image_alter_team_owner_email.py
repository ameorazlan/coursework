# Generated by Django 4.1.1 on 2022-12-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_rename_team1_table_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner_email',
            field=models.EmailField(max_length=100),
        ),
    ]