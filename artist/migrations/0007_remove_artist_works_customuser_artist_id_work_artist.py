# Generated by Django 4.2.7 on 2023-12-03 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0006_rename_name_artist_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='works',
        ),
        migrations.AddField(
            model_name='customuser',
            name='artist_id',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='work',
            name='artist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='artist.artist'),
        ),
    ]
