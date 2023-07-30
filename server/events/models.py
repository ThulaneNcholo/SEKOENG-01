from django.db import models

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