# Generated by Django 4.0.2 on 2024-08-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_remove_moviesession_cinema_hall_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesession',
            name='cinema_hall',
        ),
        migrations.AddField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ManyToManyField(to='db.CinemaHall'),
        ),
        migrations.RemoveField(
            model_name='moviesession',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviesession',
            name='movie',
            field=models.ManyToManyField(to='db.Movie'),
        ),
    ]
