# Generated by Django 5.0.2 on 2024-09-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChildB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('m2m', models.ManyToManyField(related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='myapp.othermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('m2m', models.ManyToManyField(related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='myapp.othermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
