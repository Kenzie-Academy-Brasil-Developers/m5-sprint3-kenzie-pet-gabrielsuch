from django.urls import path
from animals.views import AnimalView, AnimalIDView

urlpatterns = [
    path("", AnimalView.as_view()),
    path("<int:animal_id>", AnimalIDView.as_view())
]