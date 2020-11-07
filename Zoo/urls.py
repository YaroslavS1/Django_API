from django.urls import path
from .views import AnimalView, PlaceView, ZookeeperView

app_name = "animals"

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('place/', PlaceView.as_view()),
    path('zookeeper/', ZookeeperView.as_view())
]

