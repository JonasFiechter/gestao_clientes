from django.urls import path
from .views import MyView3, persons_list, MyView4, MyView5, MyView6
from .views import persons_new
from .views import persons_update
from .views import persons_delete


urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('person_list/', MyView3.as_view(), name="person_list_cbv"),
    path('person/<int:pk>/', MyView4.as_view(), name='person_detail'),
    path('person_create/', MyView5.as_view(), name='person_create'),
    path('person_update/<int:pk>', MyView6.as_view(), name='person_update_cbv'),
]