# Generated by Django 4.2.2 on 2023-07-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activitiesmodel_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiesmodel',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]