# Generated by Django 4.2.7 on 2023-12-03 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0007_remove_artist_works_customuser_artist_id_work_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='artist_id',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist'),
        ),
    ]
