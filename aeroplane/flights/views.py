from django.shortcuts import render
from .models import Flight,Passenger
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,"flights/index.html",{"flights":Flight.objects.all()})


def flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request,"flights/flight.html",{"flight":flight,
    "passengers":passengers,"non_passengers": non_passengers})

def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight.id,)))

