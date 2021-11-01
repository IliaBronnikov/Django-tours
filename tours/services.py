def range_prices_nights_tours(tours: list) -> list:
    range_price = []
    range_nights = []
    for tour in tours:
        range_nights.append(tour.nights)
        range_price.append(tour.price)
    nights = {"max": range_nights[-1], "min": range_nights[0]}
    prices = {"max": range_price[-1], "min": range_price[0]}
    return prices, nights
