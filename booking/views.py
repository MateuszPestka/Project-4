from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking

# Create your views here.


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(approved=True).order_by("time")
    template_name = "index.html"


class BookingDetail(View):

    def get(self, request, first_name, *args, **kwargs):
        queryset = Booking().objects.filter(approved=True)
        booking = get_object_or_404(queryset, first_name=first_name)

        return render(
            request,
            "post_detail.html",
            {
                "booking": booking,
            },
        )
