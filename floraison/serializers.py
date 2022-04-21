from django.contrib.auth.models import User
from rest_framework import serializers
from floraison.models import item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
