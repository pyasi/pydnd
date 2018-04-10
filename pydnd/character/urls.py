from django.urls import path
from .views import AbilityScoreList, SkillList, GetAbilityScore, GetSkill

urlpatterns = [
    path("ability_scores/", AbilityScoreList.as_view(), name="ability_scores"),
    path("ability_scores/<str:name_or_id>/", GetAbilityScore.as_view(), name="ability_scores"),
    path("skills/", SkillList.as_view(), name="skills"),
    path("skills/<str:name_or_id>/", GetSkill.as_view(), name="skills"),
]
