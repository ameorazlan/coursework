# Generated by Django 4.1.1 on 2022-12-02 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('owner_email', models.CharField(max_length=100)),
            ],
        ),
    ]
