from django.shortcuts import render
from rest_framework import generics
from api.models import Country, Region
from api.serializers import CountrySerializer


class CountryCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
