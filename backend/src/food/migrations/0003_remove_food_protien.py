# Generated by Django 3.1.7 on 2021-04-16 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='protien',
        ),
    ]
