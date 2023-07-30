from django.shortcuts import render
from activities.models import ActivitiesModel
from datetime import datetime

# Create your views here.


def ActivitiesView(request):
    activities = ActivitiesModel.objects.all()

    context = {
        "activities": activities
    }

    return render(request, 'activities/activities.html', context)


def ActivityDetailsView(request, id):
    activity = ActivitiesModel.objects.get(id=id)

    context = {
        "activity": activity,
    }

    return render(request, 'activities/activityDetails.html', context)
