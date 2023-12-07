from django.urls import path
from .views import Play, Last

urlpatterns = [
    path('play/', Play),
    path('last/', Last),
]
