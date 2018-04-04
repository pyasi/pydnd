from django.urls import path
from .views import LanguageList, ConditionList, DamageTypeList

urlpatterns = [
    path("languages/", LanguageList.as_view(), name="languages"),
    path("conditions/", ConditionList.as_view(), name="conditions"),
    path("damagetypes/", DamageTypeList.as_view(), name="damagetypes"),
]
