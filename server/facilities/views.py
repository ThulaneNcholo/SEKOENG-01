from django.shortcuts import render
from .models import FacilityModel

# Create your views here.


def FacilitiesView(request):
    facilities = FacilityModel.objects.all()

    context = {
        "facilities": facilities
    }

    return render(request, 'facilities/facilities.html', context)
