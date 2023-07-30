
from django.urls import path
from .import views

urlpatterns = [
    path('Accommodation', views.AccomodationView, name='Accommodation'),
    path('details-view/<int:id>', views.CottageDetailsView, name='details-view'),
    path('room-booking/<int:id>', views.BookCottageView, name='room-booking'),
    path('reserve/<int:id>', views.CottageInfoView, name='reserve'),
    path('message', views.MessageView, name='message'),
]
