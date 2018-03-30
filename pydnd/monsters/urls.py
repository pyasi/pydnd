from django.urls import path
from .views import MonsterList, MonsterGet, MonsterActionsList, MonsterSpecialAbilityList

urlpatterns = [
    path("monsters", MonsterList.as_view(), name="monsters"),
    path("monsters/<str:name_or_id>", MonsterGet.as_view(), name="monster_get"),
    path("monsters/<str:name_or_id>/actions", MonsterActionsList.as_view(), name="monster_actions"),
    path("monsters/<str:name_or_id>/special_abilities", MonsterSpecialAbilityList.as_view(), name="monster_abilities")
]
