from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from floraison import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    #floraison/item# returns the item #
    path('item<int:item_id>/', views.item),
    path('', include(router.urls)),
]