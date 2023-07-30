
from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('details/<int:id>', views.RoomDetailsView, name='details'),
    path('about', views.AboutUsView, name='about'),
    path('contact', views.ContactView, name='contact'),
    path('gallary', views.GallaryView, name='gallary'),
]
