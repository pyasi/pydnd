from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from .models import Equipment, Armor, Weapon, EquipmentSubCategory, EquipmentCategory
from .serializers import EquipmentListSerializer, ArmorListSerializer, WeaponListSerializer,EquipmentSerializer, EquipmentSubCategorySerializer, EquipmentCategorySerializer


class EquipmentList(APIView):
   def get(self, request):
        equipment = Equipment.objects.all()
        data = EquipmentListSerializer(equipment, many=True).data
        return Response(data)



class EquipmentCategoryList(generics.ListCreateAPIView):
    queryset = EquipmentCategory.objects.all()
    serializer_class =  EquipmentCategorySerializer


class EquipmentCategoryGet(APIView):

    serializer_class = EquipmentCategorySerializer

    def get(self, request, name_or_id):
        return get_equipment_category(name_or_id)


def get_equipment_category(name_or_id):

    if name_or_id.isdigit():
        queryset = EquipmentCategory.objects.get(id=int(name_or_id))
    else:
        queryset = EquipmentCategory.objects.get(name__iexact=name_or_id)
    return Response(model_to_dict(queryset), status=status.HTTP_200_OK)



class EquipmentSubCategoryList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        equipment_category = create_attribute(data, 'equipment_category', EquipmentCategorySerializer, EquipmentCategory)

        equipment_sub_category = EquipmentSubCategorySerializer(data=data)

        if equipment_sub_category.is_valid():
            equipment_sub_object = equipment_sub_category.save()
        else:
            equipment_sub_object = get_object_or_404(EquipmentSubCategory, name=equipment_sub_category.initial_data['name'])

        equipment_sub_object.equipment_category_set.add(equipment_category)

        return Response(data, status=status.HTTP_200_OK)

    queryset = EquipmentSubCategory.objects.all()
    serializer_class = EquipmentSubCategorySerializer


class ArmorList(APIView):
    def get(self, request):
        armor = Armor.objects.all()
        data = ArmorListSerializer(armor, many=True).data
        return Response(data)


class WeaponList(APIView):
    def get(self, request):
        weapon = Weapon.objects.all()
        data = WeaponListSerializer(weapon, many=True).data
        return Response(data)



def create_attribute(data, attribute_name, serializer, model_type):
    monster_attributes = []
    attributes = data.pop(attribute_name)
    for attribute in attributes:
        attribute_model = serializer(data=attribute)
        if attribute.isdigit():
            monster_attributes.append(get_object_or_404(model_type, id=int(attribute)))
        else:
            monster_attributes.append(get_object_or_404(model_type, name__iexact=attribute))

    return monster_attributes
