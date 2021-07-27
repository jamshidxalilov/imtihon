from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)



