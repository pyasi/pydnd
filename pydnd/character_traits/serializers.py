from rest_framework import serializers
from .models import Race, SubRace, Class, SubClass


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


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'


class ClassListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = ('id', 'name')


class SubClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubClass
        fields = '__all__'


class SubClassListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubClass
        fields = '__all__'
