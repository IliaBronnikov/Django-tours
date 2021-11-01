import datetime

import factory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyDate
from tours.models import Departure, Tour


class DepartureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Departure

    title = FuzzyText()
    code = FuzzyText()


class TourFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tour

    title = factory.Sequence(lambda n: f"Tour {n}")
    description = FuzzyText()
    departure = factory.SubFactory(DepartureFactory)
    picture = FuzzyText()
    price = FuzzyInteger(low=0)
    stars = FuzzyInteger(low=1)
    nights = FuzzyInteger(low=1)
    date = FuzzyDate(start_date=datetime.date(year=2000, month=1, day=1))
