from django.db import models

# Create your models here.


class RoomPackageModel(models.Model):
    room_name = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    discount_pirce = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    breakfast = models.CharField(
        max_length=200, null=True, blank=True, default='No')

    def __str__(self):
        return self.room_name


class RoomsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description_sm = models.TextField(blank=True)
    description = models.TextField(blank=True)
    people = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    breakfast_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    discount_pirce = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    package = models.ManyToManyField(
        RoomPackageModel, blank=True, default=None, related_name='package_model')
    image_main = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image1 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
