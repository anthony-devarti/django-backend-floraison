from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from floraison.serializers import UserSerializer, ItemSerializer
from .models import item

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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

