from django.shortcuts import render
from .models import *

# Create your views here.


def EventsListView(request):
    events = EventsModel.objects.all()

    context = {
        "events": events
    }
    return render(request, 'events/eventsList.html', context)
