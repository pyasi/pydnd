from django.urls import path
from .views import ArmorList, WeaponList, EquipmentCategoryList, EquipmentSubCategoryList, EquipmentCategoryGet,EquipmentSubCategoryGet, EquipmentList, EquipmentGet,ArmorCategoryList,ArmorGet, WeaponPropertyList,WeaponPropertyGet,WeaponCategoryList, WeaponList, WeaponGet

urlpatterns = [
    path("armor/", ArmorList.as_view(), name="armor"),
    path("equipment/", EquipmentList.as_view(), name="equipment"),
    path("weapons/", WeaponList.as_view(), name="weapon"),
    path("equipment_category/", EquipmentCategoryList.as_view(), name="equipment_category"),
    path("equipment_category/<str:name_or_id>/", EquipmentCategoryGet.as_view(), name="equipment_category_get"),
    path("equipment_subcategory/", EquipmentSubCategoryList.as_view(), name="equipment_subcategory"),
    path("equipment_subcategory/<str:name_or_id>/", EquipmentSubCategoryGet.as_view(), name="equipment_subcategory_get"),
    path("equipment/", EquipmentList.as_view(), name="equipment"),
    path("equipment/<str:name_or_id>/", EquipmentGet.as_view(), name="equipment_get"),
    path("armor/", ArmorList.as_view(), name="armor"),
    path("armor/<str:name_or_id>/", ArmorGet.as_view(), name="armor_get"),
    path("armor_category/", ArmorCategoryList.as_view(), name="armor_category"),
    path("weapon_property/", WeaponPropertyList.as_view(), name="weapon_property"),
    path("weapon_property/<str:name_or_id>/", WeaponPropertyGet.as_view(), name="weapon_property_get"),
    path("weapon_category/", WeaponCategoryList.as_view(), name="weapon_category"),
    path("weapon/", WeaponList.as_view(), name="weapon"),
    path("weapon/<str:name_or_id>/", WeaponGet.as_view(), name="weapon_get")
]
