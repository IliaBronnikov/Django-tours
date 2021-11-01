from tours.services import range_prices_nights_tours
import pytest


@pytest.mark.django_db()
def test_range_prices_nights_tours(departure_factory, tour_factory):
    depart1 = departure_factory()
    depart2 = departure_factory()
    tour1 = tour_factory(departure=depart1)
    tour2 = tour_factory(departure=depart2)

    prices, nights = range_prices_nights_tours([tour1, tour2])

    assert len(prices) == 2
    assert len(nights) == 2
