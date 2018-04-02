from django.urls import path
from .views import SpecialAbilityList, SpecialAbilityGet, ActionList, ActionGet

urlpatterns = [
    path("special_abilities", SpecialAbilityList.as_view(), name="special_ability"),
    path("special_abilities/<str:name_or_id>", SpecialAbilityGet.as_view(), name="special_ability"),
    path("actions", ActionList.as_view(), name="actions"),
    path("actions/<str:name_or_id>", ActionGet.as_view(), name="actions")
]
