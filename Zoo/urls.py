from django.urls import path
from .views import AnimalView

app_name = "animals"

urlpatterns = [
    path('animals/', AnimalView.as_view()),
]

