from django.urls import path
from .views import LanguageList, ConditionList, DamageTypeList, MagicSchoolList

urlpatterns = [
    path("languages/", LanguageList.as_view(), name="languages"),
    path("conditions/", ConditionList.as_view(), name="conditions"),
    path("damage_types/", DamageTypeList.as_view(), name="damagetypes"),
    path("magic_schools/", MagicSchoolList.as_view(), name="magicschools"),
]
