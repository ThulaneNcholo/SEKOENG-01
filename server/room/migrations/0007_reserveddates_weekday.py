# Generated by Django 4.2.2 on 2023-08-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_reservedroommodel_check_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveddates',
            name='weekday',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
