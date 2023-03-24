from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('<slug:slug_menu>', menu, name='menu'),
    path('<slug:slug_menu>/<slug:slug_item>/', item, name='item'),
    path('<slug:slug_menu>/<slug:slug_item>/<slug:slug_subitem>/',subitem, name='subitem'),
]
