# Generated by Django 5.0 on 2024-06-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_taches_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='taches',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
