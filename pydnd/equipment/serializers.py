from rest_framework import serializers
from .models import Equipment, Weapon, Armor, EquipmentCategory, EquipmentSubCategory, ArmorCategory, WeaponCategory, WeaponProperty


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id','name')


class EquipmentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentCategory
        fields = ('id', 'name')


class EquipmentSubCategorySerializer(serializers.ModelSerializer):

    equipment_category = EquipmentCategorySerializer(read_only=True)

    class Meta:
        model = EquipmentSubCategory
        fields = ('id','name','equipment_category')


class EquipmentSubCategoryListSerializer(serializers.ModelSerializer):


    class Meta:
        model = EquipmentSubCategory
        fields = ('id','name','equipment_category')


class ArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = '__all__'



class WeaponListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ('id', 'name')




class ArmorCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArmorCategory
        fields = ('id', 'name')


class WeaponCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponCategory
        fields = '__all__'


class ArmorListSerializer(serializers.ModelSerializer):

    armor_category=ArmorCategorySerializer(read_only=True)

    class Meta:
        model = Armor
        fields = ('id', 'name', 'armor_category')


class WeaponPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponProperty
        fields = ('id','name')



class WeaponSerializer(serializers.ModelSerializer):

    weapon_category = WeaponCategorySerializer
    weapon_property = WeaponPropertySerializer

    class Meta:
        model = Weapon
        fields = '__all__'
