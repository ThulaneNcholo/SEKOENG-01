# Generated by Django 4.2.2 on 2023-07-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activitiesmodel_count_down_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitiesmodel',
            name='event_date',
            field=models.DateField(null=True),
        ),
    ]