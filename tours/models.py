from django.db import models


class Departure(models.Model):
    class Meta:
        verbose_name = "Город вылета"
        verbose_name_plural = "Города вылета"

    code = models.CharField("код города вылета", max_length=64)
    title = models.CharField("город вылета", max_length=64)


class Tour(models.Model):
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    title = models.CharField("специальность", max_length=64)
    description = models.TextField("описание")
    departure = models.ForeignKey(
        Departure,
        verbose_name="город вылета",
        on_delete=models.CASCADE,
        related_name="tours",
    )
    picture = models.TextField("логотип")
    price = models.IntegerField("цена")
    stars = models.IntegerField("количество звезд")
    country = models.CharField("страна", max_length=64)
    nights = models.IntegerField("количество ночей")
    date = models.CharField("дата вылета", max_length=64)
