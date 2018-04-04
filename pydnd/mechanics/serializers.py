from rest_framework import serializers
from .models import Language, Condition, DamageType


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'


class DamageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageType
        fields = '__all__'