# Generated by Django 5.0.2 on 2024-09-28 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_alter_membership_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='date_joined',
        ),
    ]
