from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equipment, Armor, Weapon
from .serializers import EquipmentListSerializer, ArmorListSerializer, WeaponListSerializer


class EquipmentList(APIView):
    def get(self, request):
        equipment = Equipment.objects.all()
        data = EquipmentListSerializer(equipment, many=True).data
        return Response(data)

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
