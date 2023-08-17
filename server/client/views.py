from django.shortcuts import render
from activities.models import *
from room.models import *
from packages.models import *
from events.models import *
from facilities.models import *

from datetime import datetime
from django.db.models import F, ExpressionWrapper, DateField

# Create your views here.


def IndexView(request):

    rooms = RoomsModel.objects.all()
    packages = PackagesModel.objects.all()
    events = EventsModel.objects.all()
    blog = BlogModel.objects.all()
    facilities = FacilityModel.objects.all()[:3]

    # Get the current date and time
    current_datetime = datetime.now()
    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, and so on)
    day_of_week = current_datetime.weekday()

    # Check if the day falls on Monday to Thursday (0 to 3)
    if day_of_week <= 3:
        week_day = 'weekday'
    else:
        week_day = 'weekend'

    activities = ActivitiesModel.objects.all()
    for i in activities:
        event_date = i.event_date
        if event_date:
            # Get today's date.
            today = datetime.now().date()
            # Calculate the remaining days.
            days_remaining = (event_date - today).days
            # Assign the calculated remaining days to the activity object.
            i.remaining_days = days_remaining

    context = {
        "activities": activities,
        "rooms": rooms,
        "packages": packages,
        "events": events,
        "facilities": facilities,
        "week_day" : week_day,
        "blog" : blog
    }

    return render(request, 'client/index.html', context)


def RoomDetailsView(request, id):
    room = RoomsModel.objects.get(id=id)

    context = {
        "room": room
    }

    return render(request, 'client/roomDetails.html', context)


def AboutUsView(request):
    return render(request, 'client/about.html')


def ContactView(request):
    return render(request, 'client/contact.html')


def GallaryView(request):
    return render(request, 'client/gallary.html')
