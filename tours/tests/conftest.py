from pytest_factoryboy import register

from tours.tests.factories import (
    DepartureFactory,
    TourFactory,
)

register(DepartureFactory)
register(TourFactory)
