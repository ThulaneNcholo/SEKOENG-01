from django.shortcuts import render
from .models import *

# Create your views here.


def EventsListView(request):
    events = EventsModel.objects.all()
    blog = BlogModel.objects.all()

    context = {
        "events": events,
        "blog": blog
    }
    return render(request, 'events/eventsList.html', context)


def EventDetailsView(request, id):
    event = BlogModel.objects.get(id=id)

    context = {
        "event": event
    }
    return render(request, 'events/eventsDetails.html', context)
