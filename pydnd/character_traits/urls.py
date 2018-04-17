from django.urls import path
from .views import *

urlpatterns = [
    path("races/", RaceList.as_view(), name="races"),
    path("races/<str:name_or_id>/", GetRace.as_view(), name="races"),
    path("subraces/", SubRaceList.as_view(), name="subraces"),
    path("subraces/<str:name_or_id>/", GetSubRace.as_view(), name="subraces"),
]
