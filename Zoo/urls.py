from django.urls import path
from .views import AnimalView, PlaceView

app_name = "animals"

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('place/', PlaceView.as_view())
]

