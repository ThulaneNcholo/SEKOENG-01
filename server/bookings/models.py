from django.db import models
from room.models import *

# Create your models here.


class BookingCateredModel(models.Model):
    ref = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    breakfast = models.CharField(
        max_length=200, null=True, blank=True, default='No')
    lunch = models.CharField(max_length=200, null=True,
                             blank=True, default='No')
    dinner = models.CharField(
        max_length=200, null=True, blank=True, default='No')
    breakfastFee = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    lunchFee = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    dinnerFee = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ref


class BookedModel(models.Model):
    uuid = models.CharField(max_length=200, null=True, blank=True)
    ref = models.CharField(max_length=200, null=True, blank=True)
    room = models.ForeignKey(RoomsModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='booked_room')
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    payment_status = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    status = models.CharField(
        max_length=200, null=True, blank=True, default='Cart')
    guests = models.IntegerField(null=True, blank=True)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    room_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    food_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    catered = models.ManyToManyField(
        BookingCateredModel, blank=True, default=None, related_name='catered_food')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ref


# class PendingBookingModel(models.Model):
#     uuid_ref = models.CharField(max_length=200, null=True, blank=True)
