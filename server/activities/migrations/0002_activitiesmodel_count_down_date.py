# Generated by Django 4.2.2 on 2023-07-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitiesmodel',
            name='count_down_date',
            field=models.DateTimeField(null=True),
        ),
    ]
