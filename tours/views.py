from django.shortcuts import render
from django.views import View
from tours.models import Departure, Tour
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.services import range_prices_nights_tours

# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tours/index.html", context={"data": Tour.objects.all()})


class DepartureView(View):
    def get(self, request, city, *args, **kwargs):
        tours = Tour.objects.filter(departure__code=city)
        number_tours = tours.count()
        departure = getattr(Departure.objects.get(code=city), "title")
        prices, nights = range_prices_nights_tours(tours)
        return render(
            request,
            "tours/departure.html",
            context={
                "tours": tours,
                "price": prices,
                "night": nights,
                "number_tours": number_tours,
                "departure": departure,
            },
        )


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        return render(
            request,
            "tours/tour.html",
            context={"tour": Tour.objects.get(id=id)},
        )


def custom_handler404(request, exceptions):
    return HttpResponseNotFound("Sorry, I'm tired")


def custom_handler500(request):
    return HttpResponseServerError("Please, try another address, that is wrong")
