from django.urls import path
from .views import my_logout, MyView


urlpatterns = [
    path('', MyView.as_view(), name="home"),
    path('logout/', my_logout, name="logout"),
]