from django.urls import path
from .views import SpecialAbilityList, ActionList

urlpatterns = [
    path("special_abilities", SpecialAbilityList.as_view(), name="special_ability"),
    path("actions", ActionList.as_view(), name="actions")
]
