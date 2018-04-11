from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from django.http import Http404
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .models import Equipment, Armor, Weapon, EquipmentSubCategory, EquipmentCategory,ArmorCategory, WeaponProperty
from .serializers import EquipmentListSerializer, ArmorListSerializer, WeaponListSerializer,EquipmentSerializer, EquipmentSubCategorySerializer, EquipmentCategorySerializer,EquipmentSubCategoryListSerializer, EquipmentListSerializer, ArmorSerializer, ArmorCategorySerializer,WeaponPropertySerializer



#List of all equipment
class EquipmentList(APIView):

   def get(self, request):
        equipment = Equipment.objects.all()
        data = EquipmentListSerializer(equipment, many=True).data
        return Response(data)


#List of all equipment categories
class EquipmentCategoryList(generics.ListCreateAPIView):

    queryset = EquipmentCategory.objects.all()
    serializer_class =  EquipmentCategorySerializer


#Get for specific equipment category
class EquipmentCategoryGet(APIView):

    serializer_class = EquipmentCategorySerializer

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(EquipmentCategory, pk = int(name_or_id))
        else:
            queryset = get_object_or_404(EquipmentCategory, name = name_or_id)

        return Response(model_to_dict(queryset), status=status.HTTP_200_OK)


#Get for specific equipment sub categories
class EquipmentSubCategoryGet(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(EquipmentSubCategory, pk = int(name_or_id))
        else:
            queryset = get_object_or_404(EquipmentSubCategory, name = name_or_id)

        equipment_category = get_object_or_404(EquipmentCategory, pk = int(queryset.equipment_category.id))

        try:

            queryset_dict = {}
            queryset_dict["id"]=queryset.id
            queryset_dict["name"]=queryset.name
            queryset_dict["desc"]=queryset.desc

            equipment_category_dict = {}
            equipment_category_dict["id"]=equipment_category.id
            equipment_category_dict["name"]=equipment_category.name

        except KeyError:
            raise Http404

        queryset_dict["equipment_category"] = equipment_category_dict

        return Response(queryset_dict, status=status.HTTP_200_OK)


#TODO Remove Post
#List of equipment sub categories
class EquipmentSubCategoryList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        equipment_category_name = data.pop("equipment_category")

        equipment_category_object = get_object_or_404(EquipmentCategory, name = equipment_category_name)

        equipment_sub_category = EquipmentSubCategorySerializer(data=data)

        if equipment_sub_category.is_valid():
            equipment_sub_object = equipment_sub_category.save()
        else:
            equipment_sub_object = get_object_or_404(EquipmentSubCategory, name=equipment_sub_category.initial_data['name'])

        equipment_sub_object.equipment_category = equipment_category_object

        equipment_sub_object.save()

        return Response(data, status=status.HTTP_200_OK)

    queryset = EquipmentSubCategory.objects.all()
    serializer_class = EquipmentSubCategorySerializer


#TODO Remove Post
#List of all equipment
class EquipmentList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        equipment_subcategory_name = data.pop("equipment_category")

        equipment_subcategory_object = get_object_or_404(EquipmentSubCategory, name = equipment_subcategory_name)

        equipment= EquipmentSerializer(data=data)

        if equipment.is_valid():
            equipment_object = equipment.save()
        else:
            equipment_object = get_object_or_404(Equipment, name=equipment.initial_data['name'])

        equipment_object.equipment_category = equipment_subcategory_object

        equipment_object.save()

        return Response(data, status=status.HTTP_200_OK)

    queryset = Equipment.objects.all()
    serializer_class = EquipmentListSerializer


#Get for specific equipment
class EquipmentGet(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(Equipment, pk = int(name_or_id))
        else:
            queryset = get_object_or_404(Equipment, name = name_or_id)


        equipment_subcategory = get_object_or_404(EquipmentSubCategory, pk =int(queryset.equipment_category.id))

        equipment_category = get_object_or_404(EquipmentCategory, pk = int(equipment_subcategory.equipment_category.id))

        queryset_dict = {}
        try:

            queryset_dict["id"]=queryset.id
            queryset_dict["name"]=queryset.name
            queryset_dict["cost_quantity"]=queryset.cost_quantity
            queryset_dict["cost_denom"]=queryset.cost_denom

            equipment_subcategory_dict ={}
            equipment_subcategory_dict["id"] = equipment_subcategory.id
            equipment_subcategory_dict["name"] = equipment_subcategory.name

            equipment_category_dict = {}
            equipment_category_dict["id"]=equipment_category.id
            equipment_category_dict["name"]=equipment_category.name

        except KeyError:
            raise Http404

        queryset_dict["equipment_subcategory"]=equipment_subcategory_dict
        queryset_dict["equipment_category"]=equipment_category_dict

        return Response(queryset_dict, status=status.HTTP_200_OK)


class WeaponList(APIView):

    def get(self, request):
        weapon = Weapon.objects.all()
        data = WeaponListSerializer(weapon, many=True).data
        return Response(data)


#TODO Remove Post
#List of equipment sub categories
class ArmorList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        armor_category = get_attribute_by_name(data, 'armor_category', ArmorCategory)

        armor = ArmorSerializer(data=data)
        if armor.is_valid():
            armor_object = armor.save()
            armor_object.armor_category = armor_category
            armor_object = armor_object.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(model_to_dict(armor_object))

    queryset = Armor.objects.all()
    serializer_class = ArmorListSerializer


class ArmorGet(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(Armor, pk = int(name_or_id))
        else:
            queryset = get_object_or_404(Armor, name = name_or_id)

        armor_category = get_object_or_404(ArmorCategory, pk =int(queryset.armor_category.id))

        queryset_dict = model_to_dict(queryset)

        armor_category_dict = model_to_dict(armor_category)

        queryset_dict["armor_category"] = armor_category_dict

        return Response(queryset_dict, status=status.HTTP_200_OK)


class ArmorCategoryList(generics.ListCreateAPIView):

    queryset = ArmorCategory.objects.all()
    serializer_class = ArmorCategorySerializer

class WeaponPropertyList(generics.ListCreateAPIView):

    queryset = WeaponProperty.objects.all()
    serializer_class = WeaponPropertySerializer

class WeaponPropertyGet(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(WeaponProperty, pk = int(name_or_id))
        else:
            queryset = get_object_or_404(WeaponProperty, name = name_or_id)

        queryset_dict = model_to_dict(queryset)

        return Response(queryset_dict, status=status.HTTP_200_OK)

def get_attribute_by_name(data, attribute_name, model_type):
    attribute_value = data.pop(attribute_name)
    attribute_model = get_object_or_404(model_type, name__iexact=attribute_value)
    return attribute_model
