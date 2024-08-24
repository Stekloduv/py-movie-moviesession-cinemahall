# Generated by Django 4.0.2 on 2024-08-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_rename_genre_movie_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesession',
            name='cinema_hall',
        ),
        migrations.AddField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='db.cinemahall'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='moviesession',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='db.movie'),
            preserve_default=False,
        ),
    ]
