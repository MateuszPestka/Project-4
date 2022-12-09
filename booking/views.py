from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(approved=True).order_by("time")
    template_name = "index.html"
