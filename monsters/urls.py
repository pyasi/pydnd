from django.urls import path
from .apiviews import MonsterList, MonsterGet, SpecialAbilityList, ActionList, MonsterActionsList
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("monsters", MonsterList.as_view(), name="monsters"),
    path("monsters/<str:name_or_id>", MonsterGet.as_view(), name="monster_get"),
    path("monsters/<str:name_or_id>/actions", MonsterActionsList.as_view(), name="monster_get"),
    path("special_abilities", SpecialAbilityList.as_view(), name="special_ability"),
    path("actions", ActionList.as_view(), name="actions")
]
