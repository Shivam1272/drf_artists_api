# Generated by Django 4.2.7 on 2023-12-03 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0009_remove_customuser_artist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
