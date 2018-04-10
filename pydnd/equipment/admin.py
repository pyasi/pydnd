from django.contrib import admin
from .models import Weapon, WeaponProperty, Armor, Equipment, EquipmentCategory, EquipmentSubCategory

# Register your models here.
admin.site.register(Weapon)
admin.site.register(WeaponProperty)
admin.site.register(Armor)
admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
admin.site.register(EquipmentSubCategory)
