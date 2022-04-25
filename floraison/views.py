from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from floraison.serializers import UserSerializer, ItemSerializer, OrderSerializer
from .models import item, order
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return HttpResponse("You're at the bakery index.")

##I need to change this so I can see more than just the item number
# def item(request, item_id):
#     return HttpResponse("You're looking at %s" % item_id)


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

# class CakeViewSet(viewsets.ModelViewSet):
#     """

#     """
#     queryset = item.objects.all()
#     serializer_class = CakeSerializer

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
    API endpoint for orders
    """
    queryset = order.objects.all().order_by('-due_date')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'user']