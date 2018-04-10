from django.urls import path
from .views import AbilityScoreList, SkillList

urlpatterns = [
    path("ability_scores/", AbilityScoreList.as_view(), name="ability_scores"),
    path("skills/", SkillList.as_view(), name="skills"),
]
