from rest_framework import serializers
from .models import Language, Condition, DamageType


class LanguageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ConditionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'


class DamageTypeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageType
        fields = '__all__'