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


class PricesModel(models.Model):
    room_pirces = models.CharField(
        max_length=200, null=True, blank=True, default='room_prices')
    room_only = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    room_breakfast = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    room_weekend = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    room_weeknd_breakfast = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    room_original_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    room_original_breakfast = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.room_pirces


class RoomsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description_sm = models.TextField(blank=True)
    description = models.TextField(blank=True)
    people = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    room_prices = models.ForeignKey(PricesModel, null=True, on_delete=models.CASCADE,
                                    blank=True, default=None, related_name='room_prices')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    week_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    weekend_price = models.DecimalField(
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


# ********  Booking models start *********
class ReservedDates(models.Model):
    ref = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    room_pirce = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    breakfast = models.CharField(
        max_length=200, null=True, blank=True, default='No')
    breakfast_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    weekday = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ref


class ReservedRoomModel(models.Model):
    ref = models.CharField(max_length=200, null=True, blank=True)
    room = models.ForeignKey(RoomsModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='room')
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(
        max_length=200, null=True, blank=True, default='pending')
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    room_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    breakfast_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    user_dates = models.ManyToManyField(
        ReservedDates, blank=True, default=None, related_name='userdates')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ref
