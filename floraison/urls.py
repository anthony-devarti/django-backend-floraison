from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from floraison import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView
from floraison.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

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
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)