from django.urls import path
from .import views

urlpatterns = [
    path('facilities', views.FacilitiesView, name='facilities'),
]
