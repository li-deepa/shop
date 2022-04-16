from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    return render(request,"relecloud/index.html")

def about(request):
    return render(request,"relecloud/about.html")

def destinations(request):
    all_destinations=Destination.objects.all()
    context={'all_destinations':all_destinations}
    return render(request,'relecloud/destinations.html',context)