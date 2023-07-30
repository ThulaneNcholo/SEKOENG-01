# Generated by Django 4.2.2 on 2023-07-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description_sm', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('people', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
