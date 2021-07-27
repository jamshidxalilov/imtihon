from rest_framework import serializers

from api.models import Country, Region


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"
