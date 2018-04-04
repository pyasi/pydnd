from django.urls import path
from .views import ArmorList, EquipmentList, WeaponList

urlpatterns = [
    path("armor/", ArmorList.as_view(), name="armor"),
    path("equipment/", EquipmentList.as_view(), name="equipment"),
    path("weapons/", WeaponList.as_view(), name="weapon"),
]
