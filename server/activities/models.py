from django.db import models

# Create your models here.


class ActivitiesModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    price_per_person = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    count_down_date = models.DateTimeField(null=True,blank=True)
    count_description = models.TextField(blank=True)
    event_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
