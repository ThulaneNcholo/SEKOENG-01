# Generated by Django 4.2.2 on 2023-07-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_bookedmodel_guests_bookedmodel_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingcateredmodel',
            name='breakfastFee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='bookingcateredmodel',
            name='dinnerFee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='bookingcateredmodel',
            name='lunchFee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
