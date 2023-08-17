from django.contrib import admin
from .models import EventsModel, BlogModel

# Register your models here.
admin.site.register(EventsModel)
admin.site.register(BlogModel)
