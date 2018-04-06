from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from .models import Equipment, Armor, Weapon, EquipmentSubCategory, EquipmentCategory
from .serializers import EquipmentListSerializer, ArmorListSerializer, WeaponListSerializer,EquipmentSerializer, EquipmentSubCategorySerializer, EquipmentCategorySerializer,EquipmentSubCategoryLstSerializer, EquipmentListSerializer


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
        if name_or_id.isdigit():
            queryset = EquipmentCategory.objects.get(id=int(name_or_id))
        else:
            queryset = EquipmentCategory.objects.get(name__iexact=name_or_id)
        return Response(model_to_dict(queryset), status=status.HTTP_200_OK)


class EquipmentSubCategoryGet(APIView):



    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = EquipmentSubCategory.objects.get(id=int(name_or_id))
        else:
            queryset = EquipmentSubCategory.objects.get(name__iexact=name_or_id)

        equipment_category = EquipmentCategory.objects.get(id=int(queryset.equipment_category.id))

        queryset_dict = {}
        queryset_dict["id"]=queryset.id
        queryset_dict["name"]=queryset.name
        queryset_dict["desc"]=queryset.desc

        equipment_category_dict = {}
        equipment_category_dict["id"]=equipment_category.id
        equipment_category_dict["name"]=equipment_category.name

        queryset_dict["equipment_category"] = equipment_category_dict

        return Response(queryset_dict, status=status.HTTP_200_OK)



class EquipmentSubCategoryList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        equipment_category_name = data.pop("equipment_category")

        equipment_category_object = EquipmentCategory.objects.get(name=equipment_category_name)

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




class EquipmentList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        equipment_subcategory_name = data.pop("equipment_category")

        equipment_subcategory_object = EquipmentSubCategory.objects.get(name=equipment_subcategory_name)

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


class EquipmentGet(APIView):



    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = Equipment.objects.get(id=int(name_or_id))
        else:
            queryset = Equipment.objects.get(name__iexact=name_or_id)

        equipment_subcategory = EquipmentSubCategory.objects.get(id=int(queryset.equipment_category.id))
        equipment_category = EquipmentCategory.objects.get(id=int(equipment_subcategory.equipment_category.id))

        queryset_dict = {}
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

        equipment_subcategory_dict["equipment_category"] = equipment_category_dict

        queryset_dict["equipment_category"]=equipment_subcategory_dict

        return Response(queryset_dict, status=status.HTTP_200_OK)



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