from django.urls import path
from .import views

urlpatterns = [
    path('bookings/<int:id>', views.AvailabilityCheck, name='bookings'),
    path('room-check', views.CheckRoomAvailabity, name='room-check'),
    path('catered-food/<int:id>', views.CatedFoodView, name='catered-food'),
    path('confirm-booking', views.ConfirmBookingView, name='confirm-booking'),

    # New Views
    path('select-date/<int:id>', views.SelectDatesView, name='select-date'),
    path('room-availability', views.CheckRoomView, name='room-availability'),
    path('update-fee/<int:id>', views.BookingFeeView, name='update-fee'),
    path('room-confirmation', views.DetailsConfirmView, name='room-confirmation'),
    path('user-details', views.UserDetailsView, name='user-details'),
    path('complete-booking', views.CompleteBookingView, name='complete-booking'),

    # ****** BOOKING URLS **********
    path('availability-check/<int:id>',
         views.BookRoomDateView, name='availability-check'),
    path('room-availability-results', views.RoomResultsview,
         name='room-availability-results'),
    path('room-price/<int:id>', views.RoomPriceView, name='room-price'),
    path('details-confirm', views.RoomConfirmationDetailsView,
         name='details-confirm'),
    path('user-information', views.UserInformationView,
         name='user-information'),
    path('booking-completion', views.BookingCompletionView,
         name='booking-completion'),
]
