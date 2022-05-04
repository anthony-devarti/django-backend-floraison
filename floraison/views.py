from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework import permissions
from django.contrib.auth.models import User
from floraison.serializers import UserSerializer, ItemSerializer, OrderSerializer, CookieTypeSerializer, OrderItemSerializer
from .models import item, Order, cookie_type, order_item
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
def index(request):
    return HttpResponse("You're at the bakery index.")


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'category']
    search_fields = ['=name', 'category']
    ordering = ['id']

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['=name']
    ordering = ['id']
    

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Orders
    """
    queryset = Order.objects.all().order_by('-due_date')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'user']
    # permission_classes = [IsAuthenticated]
    #I may need to filter further to remove orders that have been marked as completed


class HomePageView(ListView):
    model = item
    template_name = 'home.html'

class CookieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for cookies, yo
    """
    queryset = cookie_type.objects.all()
    serializer_class = CookieTypeSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for adding order items
    """
    queryset = order_item.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['Order__user', 'Order']

# {
#     "total": 123,
#     "paid": true,
#     "user": 1,
#     "order_items": [
#         {
#             "item_id": 3,
#             "unit_price": 24.99,
#             "message": "nadlkfnajdf",
#             "special_instructions": "some"
#         },
#         {
#             "item_id": 2,
#             "unit_price": 24.99,
#             "message": "nadlkfnajdf",
#             "special_instructions": "some"
#         },
#         {
#             "item_id": 1,
#             "unit_price": 24.99,
#             "message": "nadlkfnajdf",
#             "special_instructions": "some"
#         }
#     ]
# }

    @action(detail=False, methods=['POST'], name='Create orders')
    def create_orders(self, request):
        print(request.data)
        order_items_data = request.data.pop('order_items')

        user_id = request.data.pop('user')
        user = User.objects.get(pk=user_id)

        order = Order.objects.create(user=user, **request.data)
        for oi in order_items_data:
            name = oi.pop('name')
            id = oi.pop('id')
            product = item.objects.get(pk=id)
            order_item.objects.create(Order=order, item=product, **oi)
            ##returning an httpresponse
        return HttpResponse(order)

# class CustomerOrderViewSet(NestedViewSetMixin, ModelViewSet):
#     """
#     For orders with nested serialization
#     """
#     queryset = order.objects.all()
#     serializer_class = OrderSerializer

##the goal is to create an api endpoint that can receive a shopping cart array, create a row on the order table, then add each item in the shopping cart array to the order items table


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer