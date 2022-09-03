from django.urls import path
from .views import home, my_logout, MyView, MyView2


urlpatterns = [
    path('', MyView.as_view(), name="home"),
    path('2', MyView2.as_view(), name="home2"),
    path('logout/', my_logout, name="logout"),
]