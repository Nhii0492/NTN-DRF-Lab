# Generated by Django 5.0.2 on 2024-09-28 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_person_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('home_group', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.date(2000, 1, 1), null=True),
        ),
    ]
