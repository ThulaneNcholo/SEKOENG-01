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
    facilities = FacilityModel.objects.all()[:3]

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
        "facilities": facilities
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
