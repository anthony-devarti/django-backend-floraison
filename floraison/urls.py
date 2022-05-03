from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from floraison import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'Orders', views.OrderViewSet)
router.register(r'cookie_type', views.CookieViewSet)
router.register(r'order_item', views.OrderItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path("", HomePageView.as_view(), name="home"),
]