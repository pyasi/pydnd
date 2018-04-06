from django.urls import path
from .views import ArmorList, EquipmentList, WeaponList, EquipmentCategoryList, EquipmentSubCategoryList, EquipmentCategoryGet,EquipmentSubCategoryGet

urlpatterns = [
    path("armor/", ArmorList.as_view(), name="armor"),
    path("equipment/", EquipmentList.as_view(), name="equipment"),
    path("weapons/", WeaponList.as_view(), name="weapon"),
    path("equipment_category/", EquipmentCategoryList.as_view(), name="equipment_category"),
    path("equipment_category/<str:name_or_id>/", EquipmentCategoryGet.as_view(), name="equipment_category_get"),
    path("equipment_subcategory/", EquipmentSubCategoryList.as_view(), name="equipment_subcategory"),
    path("equipment_subcategory/<str:name_or_id>/", EquipmentSubCategoryGet.as_view(), name="equipment_subcategory_get"),

]
