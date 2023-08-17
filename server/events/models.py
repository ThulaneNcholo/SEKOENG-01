from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class EventsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    blog_section = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    host = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
