# Generated by Django 5.0.2 on 2024-09-28 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
    ]
