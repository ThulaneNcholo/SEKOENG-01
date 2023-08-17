
from django.urls import path
from .import views

urlpatterns = [
    path('events', views.EventsListView, name='events'),
    path('event-details/<int:id>', views.EventDetailsView, name='event-details'),
]
