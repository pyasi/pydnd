from django.urls import path
from .race_views import *
from .class_views import *

urlpatterns = [
    path("races/", RaceList.as_view(), name="races"),
    path("races/<str:name_or_id>/", GetRace.as_view(), name="races"),
    path("subraces/", SubRaceList.as_view(), name="subraces"),
    path("subraces/<str:name_or_id>/", GetSubRace.as_view(), name="subraces"),

    path("classes/", ClassList.as_view(), name="classes"),
    path("classes/<str:name_or_id>/", GetClass.as_view(), name="classes"),
    path("subclasses/", SubClassList.as_view(), name="subclasses"),
    path("subclasses/<str:name_or_id>/", GetSubClass.as_view(), name="subclasses"),
]
