from rest_framework import serializers
from .models import Equipment, Weapon, Armor, EquipmentCategory, EquipmentSubCategory

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentCategory
        fields = '__all__'


class EquipmentSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentSubCategory
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = '__all__'

class ArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = '__all__'


class EquipmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id', 'name')


class WeaponListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ('id', 'name')

class ArmorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = ('id', 'name')




