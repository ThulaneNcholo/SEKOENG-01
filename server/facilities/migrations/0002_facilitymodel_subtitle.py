# Generated by Django 4.2.2 on 2023-07-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitymodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
