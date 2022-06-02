from django.urls import path, include
from rest_framework import routers

from myapi import views

router = routers.DefaultRouter()   #aceasta comanda se ocupa de routare
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]