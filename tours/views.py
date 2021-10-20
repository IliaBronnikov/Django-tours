from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError

# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index_test.html', context={'tours': settings.TOURS})


class DepartureView(View):
    def get(self, request, city, *args, **kwargs):
        depart = settings.DEPARTURES[city][2::]
        filt_tours = dict(filter(lambda x: x[1]['departure'] == city, settings.TOURS.items()))
        range_price = []
        range_night = []
        for key in filt_tours:
            range_price.append(filt_tours[key]["price"])
            range_night.append(filt_tours[key]["nights"])
        number_tours = len(filt_tours)
        nights = {'max': sorted(range_night)[-1], 'min': sorted(range_night)[0]}
        prices = {'max': sorted(range_price)[-1], 'min': sorted(range_price)[0]}

        return render(request, 'tours/departure_test.html', context={'tours': filt_tours, 'departure': depart,
                                                                     'price': prices, 'night': nights, 'number_tours':
                                                                         number_tours})


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        depart = settings.DEPARTURES[settings.TOURS[id]['departure']]
        return render(request, 'tours/tour_test.html', context={'tours': settings.TOURS[id], 'departure': depart})


def custom_handler404(request, exceptions):
    return HttpResponseNotFound('Get out, fucking bullshit')


def custom_handler500(request):
    return HttpResponseServerError('Sorry, I\'m tired')
