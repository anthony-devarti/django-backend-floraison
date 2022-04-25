from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from floraison import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]