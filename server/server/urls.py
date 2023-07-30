from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('bookings/', include('bookings.urls')),
    path('activities/', include('activities.urls')),
    path('facilities/', include('facilities.urls')),
    path('room/', include('room.urls')),
    path('events/', include('events.urls')),
]
