from rest_framework import serializers
from .models import Race, SubRace


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = '__all__'


class RaceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = ('id', 'name')

class SubRaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubRace
        fields = '__all__'


class SubRaceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubRace
        fields = ('id', 'name')