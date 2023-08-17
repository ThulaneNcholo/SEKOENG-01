from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(RoomsModel)
admin.site.register(RoomPackageModel)
admin.site.register(PricesModel)
admin.site.register(ReservedDates)
admin.site.register(ReservedRoomModel)
