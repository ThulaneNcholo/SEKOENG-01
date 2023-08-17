# Generated by Django 4.2.2 on 2023-08-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_blogmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='host',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]