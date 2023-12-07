# Generated by Django 5.0 on 2023-12-06 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0001_initial'),
        ('users', '0002_rename_points_profile_rounds_played_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot_one',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot_three',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot_two',
            field=models.IntegerField(blank=True),
        ),
    ]
