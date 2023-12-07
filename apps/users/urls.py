from django.urls import path
from .views import UserList, UserNew

urlpatterns = [
    path('users/', UserList),
    path('users/new/', UserNew)
]
