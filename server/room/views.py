from django.shortcuts import render
from room.models import *
from datetime import datetime

# Create your views here.


def AccomodationView(request):
    rooms = RoomsModel.objects.all()

    context = {
        "rooms": rooms
    }

    return render(request, 'room/accomodations.html', context)


def CottageDetailsView(request, id):
    room = RoomsModel.objects.get(id=id)

    context = {
        "room": room
    }

    return render(request, 'room/cottageDetails.html', context)


def BookCottageView(request, id):
    room = RoomsModel.objects.get(id=id)

    context = {
        "room": room
    }

    return render(request, 'room/bookCottage.html', context)


def CottageInfoView(request, id):
    if request.method == 'POST':
        room = RoomsModel.objects.get(id=id)
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guest = request.POST.get('guest')

        # Convert date strings to date objects
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(checkin, date_format).date()
        date2 = datetime.strptime(checkout, date_format).date()

        daysCount = (date2 - date1).days

        total = 0
        roomPrice = room.price
        sub_total = daysCount * roomPrice
        total = total + sub_total

        context = {
            "total": total
        }

    return render(request, 'partials/cottageInfo.html', context)


def MessageView(request):
    return render(request, 'room/message.html')
