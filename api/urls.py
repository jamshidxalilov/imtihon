from django.urls import path
from api.views import CountryCreateView, CountryDeleteView, CountryListView


urlpatterns = [
    path('country/add/', CountryCreateView.as_view()),
    path('country/', CountryListView.as_view()),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view()),
]