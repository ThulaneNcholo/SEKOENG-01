from django.urls import path
from .import views

urlpatterns = [
    path('activities', views.ActivitiesView, name='activities'),
    path('activities-details/<int:id>', views.ActivityDetailsView,
         name='activities-details'),
]
